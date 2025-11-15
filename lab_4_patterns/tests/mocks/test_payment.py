import pytest
from unittest.mock import Mock, MagicMock
from src.structural.adapter import PaymentAdapter, LegacyPaymentSystem

class TestPaymentAdapter:
    def test_payment_adapter_with_mock(self):
        # Arrange
        mock_legacy_system = Mock(spec=LegacyPaymentSystem)
        mock_legacy_system.make_payment.return_value = True
        adapter = PaymentAdapter(mock_legacy_system)
        payment_details = {'card_number': '1234567890123456'}

        # Act
        result = adapter.process_payment('order123', 100.0, payment_details)

        # Assert
        assert result == True
        mock_legacy_system.make_payment.assert_called_once_with(100.0, '1234567890123456')

    def test_payment_adapter_failure(self):
        # Arrange
        mock_legacy_system = Mock(spec=LegacyPaymentSystem)
        mock_legacy_system.make_payment.return_value = False
        adapter = PaymentAdapter(mock_legacy_system)
        payment_details = {'card_number': 'invalid'}

        # Act
        result = adapter.process_payment('order124', 50.0, payment_details)

        # Assert
        assert result == False
