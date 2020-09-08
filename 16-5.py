import re

rule = r"""(

        (\d{2}|\(\d{2}\))?              # 區域號碼
        (\s|-)?                         # 區域號碼與電話號碼的分隔符號
        \d{7}(\d)                      # 電話號碼
        (\s*(ext|ext.)\s*\d{2,4})?      # 2-4位數的分機號碼

        )"""

msg = """02-88223349,(02)-26669999,02-29998888 ext 123,12345678,
           02 33887766 ext. 12222,02-1234567,02-123456789,
           23-123456
                            """

result = re.findall(rule,msg, re.VERBOSE)

for final in result:
    print(final[0])
