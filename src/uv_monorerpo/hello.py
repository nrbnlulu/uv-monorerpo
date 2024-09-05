
from amaizing import so_amaizing

def main():
    def this_fails():
        from sdk.amaizing import so_amaizing
        print(so_amaizing())
    def this_works():
        from libs.sdk.src.sdk.amaizing import so_amaizing
        print(so_amaizing())
    this_works()
    this_fails()

if __name__ == "__main__":
    main()
