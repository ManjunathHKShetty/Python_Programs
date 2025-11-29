tests = [
    {"id": 1, "status": "pass"},
    {"id": 2, "status": "fail"},
    {"id": 3, "status": "pass"},
    {"id": 4, "status": "fail"},
    {"id": 5, "status": "pass"},
]


def test_percentage_of_Test_case():
    total = len(tests)
    passed = 0

    for test in tests:
        if test["status"] == "pass":
            passed += 1

    # calculate percentage
    return (passed / total) * 100


print("Pass percentage:", test_percentage_of_Test_case(), "%")
