	#	break

	#for y in str(lastname):
		#if str(x).isdigit:
		#	info = ("Name must only consist of lette
class college:
	name=""
	top_20=False 
	#top_colleges=["Harvord", "Prinston", "Yale", "Stanford", "Dartmouth", "Cornell", "Columbia", "MIT", "Washington", "John Hopkins", "Cooper Union", "Browns", "Pennsylvania", "Chicago", "Michigan", "Duke", "Northwestern", "Vanderbilt", "Notre Dame", "Georgetown"]
	majors=["Engineering", "Civil Engineering", "Chemical Engineering", "Biomedical Engineering", "Physics", "Chemistry", "Biochemistry", "Organic Chemistry", "Computer Science", "Robotics","English", "Philosophy", "Economics", "Government", "History", "Education", "Law", "Criminal Justice", "Medicine", "Creative Writing", "Japanese", "Spanish", "Dance", "Acting", "Anatomy", "Physiology", "Genetics", "Kenesiology", "Business", "Accounting", "Financing", "Music", "Art", "Phisical Education", "Psycology", "Nero Science", "Mathimatics", "Game Development", "Premed", "Special Education", "Undecided", "British Litarature", "French Litarature", "Dentistry", "Earth Science", "Ecology", "Enviremental Conservation", "Gender Studies", "Geography", "Astronomy", "Astro Physics", "Martial Arts", "Gameing", "Music Theory", "Public Speaking", "Real Estate", "Fashion", "Sculpting", "Painting", "Asian History", "Native American History", "Asian Culture", "Anylitical Writing", "American Litarature", "Poetry", "Bird Watching", "Irish History", "Irish Litaratur", "Irish Culture", "Dancing", "Coaching", "Sports Managment", "Computing and Information Technologies"]

	engineering_majore=majors[len(range(9))]

	

	def get_user_major(request):
		major=request.GET["major"]
		return major

	def top_20_set(is_top_20):
		self.top_20=is_top_20

	def top_20_get():
		return self.top_20

	def name_set(new_name):
		self.name=new_name

	def name_get():
		return self.name 



