#!/usr/bin/env python3
"""okf_validate 的单元测试（标准库 unittest，无第三方依赖）。

用 tempfile 造夹具，验证：
 - 有 type 的合法概念不报错
 - 缺 type 的概念报"缺 type"
 - 无 frontmatter 的概念报"缺 frontmatter"
 - 指向不存在文件的链接报"断链"
 - index.md 被跳过
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import okf_validate  # noqa: E402


def write(path, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(body)


GOOD = """---
type: "Tool"
title: "Good"
description: "ok"
---
正文 [other](other.md)
"""
OTHER = """---
type: "Term"
title: "Other"
---
正文
"""
NO_TYPE = """---
title: "NoType"
---
正文
"""
NO_FM = """正文，没有 frontmatter
"""
BROKEN = """---
type: "Note"
title: "Broken"
---
指向 [missing](does-not-exist.md) 的链接
"""


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.content = os.path.join(self.tmp, 'content')
        self.concepts = os.path.join(self.content, 'concepts')
        os.makedirs(self.concepts, exist_ok=True)

    def _run(self):
        return okf_validate.validate(self.concepts, self.content)

    def test_clean_bundle_passes(self):
        write(os.path.join(self.concepts, 'good.md'), GOOD)
        write(os.path.join(self.concepts, 'other.md'), OTHER)
        errs = self._run()
        self.assertEqual(errs, [], f"expected no errors, got {errs}")

    def test_missing_type_reported(self):
        write(os.path.join(self.concepts, 'good.md'), GOOD)
        write(os.path.join(self.concepts, 'other.md'), OTHER)
        write(os.path.join(self.concepts, 'no_type.md'), NO_TYPE)
        errs = self._run()
        self.assertEqual(len(errs), 1)
        self.assertIn('no_type.md', errs[0])
        self.assertIn('type', errs[0])

    def test_no_frontmatter_reported(self):
        write(os.path.join(self.concepts, 'good.md'), GOOD)
        write(os.path.join(self.concepts, 'other.md'), OTHER)
        write(os.path.join(self.concepts, 'nofm.md'), NO_FM)
        errs = self._run()
        self.assertEqual(len(errs), 1)
        self.assertIn('nofm.md', errs[0])
        self.assertIn('frontmatter', errs[0])

    def test_links_inside_code_not_flagged(self):
        # 反引号/代码块里的 [X](./x.md) 是示例文字，不应被判为断链
        body = """---
type: "Note"
title: "Demo"
---
用标准链接 `[X](./x.md)` 举例。

```
[also-not-a-link](./y.md)
```
真实链接 [other](other.md)
"""
        write(os.path.join(self.concepts, 'good.md'), GOOD)
        write(os.path.join(self.concepts, 'other.md'), OTHER)
        write(os.path.join(self.concepts, 'demo.md'), body)
        errs = self._run()
        self.assertEqual(errs, [], f"code-span links should be ignored, got {errs}")

    def test_broken_link_reported(self):
        write(os.path.join(self.concepts, 'good.md'), GOOD)
        write(os.path.join(self.concepts, 'other.md'), OTHER)
        write(os.path.join(self.concepts, 'broken.md'), BROKEN)
        errs = self._run()
        broken = [e for e in errs if '断链' in e or 'does-not-exist' in e]
        self.assertEqual(len(broken), 1, f"expected one broken-link error, got {errs}")
        self.assertIn('broken.md', broken[0])

    def test_index_skipped(self):
        # index.md 即使内容不合规也不应被校验
        write(os.path.join(self.concepts, 'good.md'), GOOD)
        write(os.path.join(self.concepts, 'other.md'), OTHER)
        write(os.path.join(self.concepts, 'index.md'), NO_FM)
        errs = self._run()
        self.assertEqual(errs, [])


if __name__ == '__main__':
    unittest.main()
