import pytest
from predictions import app


@pytest.fixture
def client():
    return app.test_client()


def test_predictions(client):
    test_data = {
            "Gender": "Female",
            "Married": "No",
            "ApplicantIncome": 500,
            "LoanAmount": 10000000,
            "Credit_History": 1.0
    }
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": 'Rejected'}