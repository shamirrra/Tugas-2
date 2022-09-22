from django.test import TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_watch_list, show_json, show_xml

class url_testing(TestCase):

    def initial_test(self):
        self.urlToViewHtml = reverse('mywatchlist:show_watch_list')
        self.urlToViewJson = reverse('mywatchlist:show_json')
        self.urlToViewXML = reverse('mywatchlist:show_xml')

    def html_test(self):
        self.assertEqual(resolve(self.urlToViewHtml).func,show_watch_list)
        
    def json_test(self):
        self.assertEqual(resolve(self.urlToViewJson).func,show_json)

    def xml_test(self):
        self.assertEqual(resolve(self.urlToViewXML).func,show_xml)