import sys

from . import main

if sys.version_info < (3, 9, 0):
    print("Требуется Python 3.9 или выше")
    sys.exit(1)


from argparse import ArgumentParser
import asyncio


def parse_arguments():
    parser = ArgumentParser(
        prog="TeaGram", description="Юзербот",
        add_help=True
    )
    parser.add_argument("--list-optimizations",
                        action="store_true",
                        help="Вывести доступные оптимизации",
                        default=False
                        )
    parser.add_argument("-n",
                        "--no-optimizations",
                        action="store_false",
                        default=True,
                        help="Выключить использование оптимизаций"
                        )
    return parser.parse_args()


args = parse_arguments()

if args.list_optimizations:
    from . import optimizations
    optimizations_list = optimizations.apply_optimizations()
    print(f"Доступно {len(optimizations_list)} оптимизаций:")
    for o in optimizations_list:
        print(" - " + o)
    exit()

if args.no_optimizations:
    from . import optimizations
    optimizations.apply_optimizations()

if __name__ == "__main__":


    # import logging                          # РАЗКОММЕНТИРУЙТЕ ЭТО ЕСЛИ У ВАС БЕСКОНЕЧНАЯ ЗАГРУЗКА, И ОТПРАВЬТЕ ЛОГИ В САППОРТ ЧАТ https://t.me/UBteagram/974
    # logging.basicConfig(level=logging.INFO) # UNCOMMENT THIS IF YOU HAVE INFINITY LOADING, AND SEND LOGS TO SUPPORT CHAT https://t.me/UBteagram/974
    
    asyncio.run(main.main())
