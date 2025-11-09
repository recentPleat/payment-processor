import logging
from payment_processor import config
from payment_processor.services import payment_service
from payment_processor.repositories import db_repository
from payment_processor.exceptions import PaymentError

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Initialize database connection
    db_repository.initialize(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, config.DB_NAME)

    try:
        # Process payments
        payment_service.process_payments()
    except PaymentError as e:
        logger.error(f"Payment processing failed: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        # Close database connection
        db_repository.close()

if __name__ == "__main__":
    main()