from components.base_component import BaseComponent

from playwright.sync_api import Page, expect

from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page : Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page,'course-widget-title-text', 'Title')
        self.image = Image(page,'course-preview-image', 'Image')
        self.max_score = Text(page,'course-max-score-info-row-view-text', 'Max score text')
        self.min_score = Text(page,'course-min-score-info-row-view-text', 'Min score text')
        self.estimated_time = Text(page,'course-estimated-time-info-row-view-text', 'Estimated time text')

    def check_visible(self, title: str,estimate_time:str, max_score: str, min_score: str, index: int):
        self.image.check_visible(nth=index)

        self.title.check_visible(nth=index)
        self.title.have_text(title, nth=index)

        self.max_score.check_visible(nth=index)
        self.max_score.have_text(f'Max score: {max_score}',nth=index)

        self.min_score.check_visible(nth=index)
        self.min_score.have_text(f'Min score: {min_score}',nth=index)

        self.estimated_time.check_visible(nth=index)
        self.estimated_time.have_text(f'Estimated time: {estimate_time}', nth=index)
