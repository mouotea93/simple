from django.db import models

# Create your models here.
A = "A"
B = "B"
C = "C"
D = "D"
F = "F"
PASS = "PASS"
FAIL = "FAIL"

GRADE = (
		(A, 'A'),
		(B, 'B'),
		(C, 'C'),
		(D, 'D'),
		(F, 'F'),
	)

COMMENT = (
		(PASS, "PASS"),
		(FAIL, "FAIL"),
	)

LEVEL = (
		("100", 100),
		("200", 200),
		("300", 300),
		("400", 400),
		("500", 500),
	)
FIRST = "First"
SECOND = "Second"

SEMESTER = (
		(FIRST, "First"),
		(SECOND, "Second"),
	)



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/', max_length=100)
    cover = models.ImageField(upload_to='books/covers/', blank=True, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)   