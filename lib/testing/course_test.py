from Course import Course

class Test_Course:
    '''Course in Course.py'''

    # fixed test methods.
    def test_title_instance_variable(self):
        "Test setting and getting for title"
        course = Course(title="Programming Robots for Outer Space", schedule="Full-Time", description="Learn robotics")
        assert course.title == "Programming Robots for Outer Space"

    def test_schedule_instance_variable(self):
        "Test setting and getting for schedule"
        course = Course(title="Intro to AI", schedule="Full-Time", description="Learn about artificial intelligence")
        assert course.schedule == "Full-Time"

    def test_description_instance_variable(self):
        "Test setting and getting for description"
        course = Course(title="Space Navigation", schedule="Part-Time", description="Learn how to navigate in space")
        assert course.description == "Learn how to navigate in space"
