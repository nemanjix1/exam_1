#JA VRV JOS NISAM URADIO ILI NISAM DOBRO FAJL IMPORTOVAO-NE ZNAM GDE MI JE TO, PA NISAM SIGURAN DA LI RADI-PRIJAVLJUJE MI SAMO no module, drugih gresaka nisam video
from exam_lib import Book
class EBook(Book):
    def __init__(self,title, author, page_count,size,registration_code):
        super().__init__(title=title,author=author,page_count=page_count)
        self.size=size
        self._registration_code=registration_code if self._check_code(registration_code) else None
    @staticmethod 
    def _check_code(registration_code):
        if len(registration_code)==16:
            return True
        return False
    @property
    def registration_code(self, registration_code):
        return self._registration_code
      
    @registration_code.setter
    def registration_code(self, registration_code):
        self._registration_code=registration_code  if self._check_code(registration_code) else None
