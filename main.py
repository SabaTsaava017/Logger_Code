from datetime import datetime

class ValidationError(Exception):
   
    pass

class ConsoleLogger:
    DEBUG = 1
    INFO = 2
    ERROR = 3
    
    LOG_LEVELS = {
        DEBUG: "DEBUG",
        INFO: "INFO",
        ERROR: "ERROR"
    }

    def validate_message(self, message):
        if message is None:
            raise ValidationError("ლოგირების მესიჯი არ შეიძლება იყოს NULL")
        if not isinstance(message, str):
            raise ValidationError("ლოგირების მესიჯი უნდა იყოს string ტიპის")
        if not message.strip():
            raise ValidationError("ლოგირების მესიჯი არ შეიძლება იყოს ცარიელი")

    def log(self, log_type, message):
        try:
            self.validate_message(message)
            timestamp = datetime.now().isoformat()
            log_level = self.LOG_LEVELS.get(log_type, "UNKNOWN")
            print(f"[{timestamp}][{log_level}]: {message}")
        except ValidationError as e:
            print(f"[{datetime.now().isoformat()}][ERROR]: Validation Error - {e}")

class Application:
    def __init__(self):
        self.logger = ConsoleLogger()
    
    def run(self):
        self.logger.log(ConsoleLogger.INFO, "Oh my god!")
        self.logger.log(ConsoleLogger.DEBUG, "Running in debug mode.")
        self.logger.log(ConsoleLogger.ERROR, "An error occurred!")
        self.logger.log(ConsoleLogger.INFO, "")  
        self.logger.log(ConsoleLogger.ERROR, None)  

if __name__ == "__main__":
    app = Application()
    app.run()