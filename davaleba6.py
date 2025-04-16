import logging


logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide(a, b):
    logging.debug("Calling divide function with arguments: a=%s, b=%s", a, b)
    try:
        result = a / b
        logging.info("Division successful: %s / %s = %s", a, b, result)
        return result
    except ZeroDivisionError as e:
        logging.error("Division by zero error: %s", e)
    except Exception as e:
        logging.error("Unexpected error: %s", e)


divide(10, 2)
divide(5, 0)
