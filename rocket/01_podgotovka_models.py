class New_year_list(models.Model):
	nazvanie = models.CharField(max_length=60)
	quantity = models.IntegerField()
	purchased = models.BooleanField(default=False)
TEST 2