from django.test import TestCase

from django.utils import timezone
from .models import Course, Step
from django.urls import reverse   # Django2删除了django.core.urlresolvers,并移到django.urls


# Create your tests here.
class CourseModelTest(TestCase):
    def test_course_creation(self):   # 1st test
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in Python")
        now = timezone.now()
        self.assertEqual(course.created_at, now
        # self.assertLess(course.created_at, now) 会出错, 为什么?
        )


class StepModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in Python"
        )

    def test_step_creation(self):   # 2nd test
        step = Step.objects.create(
            title="Introduction to Dostests",
            description="Learn to write tests in your docstrings.",
            course=self.course
        )
        self.assertIn(step, self.course.step_set.all())

class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in Python")

        self.course2 = Course.objects.create(
            title="New Course",
            description="A new course")

        self.step = Step.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in your docstrings",
            course=self.course)

    def test_course_list_view(self):  # 3rd test
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')  # 6.5 update
        self.assertContains(resp, self.course.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail',
                                       kwargs={'pk': self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])

    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:step', kwargs={
                    'course_pk': self.course.pk,
                    'step_pk': self.step.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])


