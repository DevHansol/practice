from pay_module import version, Pay, printAuthor

if __name__ == '__main__':
    print(version)
    printAuthor()

    pay_info = Pay('A12304', 13000, "2022-06-07")
    print(pay_info.get_pay_info())
