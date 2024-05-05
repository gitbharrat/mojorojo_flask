from predictions import app
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_predict(client):
    test_data = {
        "Gender": "Female",
        "Married": "No",
        "ApplicantIncome": 500,
        "LoanAmount": 500000000,
        "Credit_History": 1.0
    }
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": 'Rejected'}

