"""
get_user_context.py
This module retrieves user-specific health information based on the user ID.
It is used in the retrieval-augmented generation (RAG) pipeline to provide context for answering user queries.

"""


def get_user_context(user_id: str) -> str:
    """
    Retrieves the user context based on the user ID.

    Args:
        user_id (str): The ID of the user.

    Returns:
        str: The context of the user.
    """

    context = {
        "u001": "Patient has type 2 diabetes and is on metformin.",  # mock user data
        "u002": "Patient is recovering from heart surgery and has a follow-up appointment next week.",
        "u003": "Patient has a history of hypertension and is currently on lisinopril.",
        "u004": "Patient is a new user with no previous medical history.",
        "u005": "Patient has allergies to penicillin and sulfa drugs.",
        "u006": "Patient is a senior citizen with multiple chronic conditions.",
        "u007": "Patient is a pediatric patient with asthma and uses an inhaler.",
        "u008": "Patient is pregnant.",
    }
    # Placeholder for actual implementation
    return context.get(user_id, "User context not found.")
