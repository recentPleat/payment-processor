import logging
from payment_processor.config import Config
from payment_processor.services import PaymentService

def main():
    logging.basicConfig(level=logging.INFO)
    config = Config()
    payment_service = PaymentService(config)

    try:
        payment_service.process_payments()
    except Exception as e:
        logging.error(f"Error processing payments: {e}")
        return 1

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())