def strict(func):
    def wrapper(*args, **kwargs):
        types = list(func.__annotations__.values())[:-1] # Дропаем тип который возвращает return
        if not all([type(args[i])==types[i] for i in range(len(args))]):
            raise TypeError
        
        return func(*args,**kwargs)
    
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

def main():
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError

if __name__ == "__main__":
    main()


