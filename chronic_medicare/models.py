from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AnalysisFile(models.Model):
    name = models.CharField(max_length=512)
    csv_file = models.FileField(upload_to='analysis-files/')
    description = models.TextField(max_length=1024, blank=True)

    class Meta:
      verbose_name_plural = "Raw Analysis Files"

    def __str__(self):
        return "{name}: {csv_file}".format(
            name=self.name,
            csv_file=self.csv_file.name.split('/')[-1])