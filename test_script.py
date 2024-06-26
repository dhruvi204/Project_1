import pytest
from content_generation_huggingface import generate_description
from recommendation_system import model

def test_generate_description():
    attributes = "Color: Red, Size: Medium, Material: Cotton, Brand: XYZ"
    description = generate_description(attributes)
    assert description is not None

def test_recommendation_model():
    assert model is not None

if __name__ == "__main__":
    pytest.main()
