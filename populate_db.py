import os
import django
from bs4 import BeautifulSoup

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # Replace with your settings file
django.setup()

from lcrportfolio_slug.products.models import Skill, Education, Project  # Import your models
from bs4 import BeautifulSoup

# HTML content (replace with the actual HTML)
html_content = """
<!DOCTYPE html>

<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Laxman Chandra Rana - Portfolio Website</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="./assets/animate.css">
    <link rel="stylesheet" href="./assets/flaticon-31.css">
    <link rel="stylesheet" href="./assets/owl.carousel.css">
    <link rel="stylesheet" href="./assets/typer.css">
    <link rel="stylesheet" href="./assets/slick-theme.css">
    <link rel="stylesheet" href="./assets/slick.css">
    <link rel="stylesheet" href="./assets/bootstrap.min.css">
    <link rel="stylesheet" href="./assets/style-31.css">
    <script src="https://kit.fontawesome.com/d59710d54e.js" crossorigin="anonymous"></script>
    <style type="text/css">@font-face {
        font-family: Roboto;
        src: url("chrome-extension://mcgbeeipkmelnpldkobichboakdfaeon/css/Roboto-Regular.ttf");
    }</style>
</head>
<body class="apihu-port-body" data-new-gr-c-s-check-loaded="14.1062.0" data-gr-ext-installed="">
    <div class="apihu-port-body-overlay"></div>
    <div class="loading-preloader" style="display: none;">
        <div id="loading-preloader">
            <div class="line_shape"></div>
            <div class="line_shape"></div>
            <div class="line_shape"></div>
            <div class="line_shape"></div>
            <div class="line_shape"></div>
            <div class="line_shape"></div>
            <div class="line_shape"></div>
            <div class="line_shape"></div>
            <div class="line_shape"></div>
            <div class="line_shape"></div>
        </div>
    </div>
    <a href="#" class="apihu-port-scroll-top" style="display: none;"><i class="fas fa-chevron-up"></i></a>
    <header class="apihu-port-header-area">
        <div class="container">
            <div class="row">
                <div class="col-xl-2 col-lg-2 col-md-2 col-3">
                    <div class="apihu-port-logo">
                        <img src="./assets/lcr.png" alt="SaaSio Portfolio">
                    </div>
                </div>
                <div class="col-xl-8 d-none d-lg-block text-center col-lg-8">
                    <div class="apihu-port-main-navigation">
                        <ul>
                            <li><a href="#">Home</a></li>
                            <li><a href="#apihu-port-resume">About</a></li>
                            <li><a href="#apihu-port-feature">Projects</a></li>
                            <li><a href="#apihu-port-pricing-area">Qualifications</a></li>
                            <li><a href="#contact-details">Contact</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-xl-2 col-lg-2 col-md-10 col-9 text-right">
                    <div class="apihu-port-header-cta">
                        <a href="https://www.instagram.com/laxmanchandrarana/">Let's Chat <i
                                class="fas fa-comment-dots"></i></a>
                    </div>
                    <div class="apihu-port-mobile-menu-hamburger">
                        <a href="#"><i class="fas fa-bars"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <div class="apihu-port-mobile-menu">
        <a href="#" class="apihu-port-menu-close"><i class="fas fa-times"></i></a>
        <a href="#" class="apihu-port-logo-wrapper"><img src="./assets/white-logo.png" alt=""></a>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#apihu-port-resume">About</a></li>
            <li><a href="#apihu-port-feature">Projects</a></li>
            <li><a href="#apihu-port-pricing-area">Qualifications</a></li>
            <li><a href="#contact-details">Contact</a></li>
        </ul>
    </div>
    <section class="apihu-port-hero-area" id="apihu-port-hero">
        <img class="apihu-port-hero-shape-1" src="./assets/hero-shape.png" alt="Shape">
        <img class="apihu-port-hero-shape-2" src="./assets/python.png" alt="Shape">
        <img class="apihu-port-hero-shape-3" src="./assets/arduino.png" alt="Shape">
        <img class="apihu-port-hero-shape-4" src="./assets/html.png" alt="Shape">
        <img class="apihu-port-hero-shape-5" src="./assets/sql.png" alt="Shape">
        <span class="apihu-port-hero-side-style-text">Laxman</span>
    </section>
    <div class="container">
        <h2>About Me</h2>
        <p>I am Laxman Chandra Rana, a full-time Associate Software Developer with strong backend development
            experience in Django REST APIs and full-stack exposure using WordPress. My projects span web development,
            automation, and Python-based desktop tools. I value clean architecture, testable code, and continuous
            learning.</p>
        <h2>Technical Skills</h2>
        <ul>
            <li><strong>Languages:</strong> Python, HTML, CSS, Embedded C</li>
            <li><strong>Libraries & Tools:</strong> Django, Docker, Postman, Tkinter, Celery, Jira Board, BitBucket, OS,
                Pandas, Git, Github, Wordpress, ODOO</li>
            <li><strong>Database:</strong> MySQL, Postgres</li>
            <li><strong>Languages Known:</strong> English, Hindi, Bengali</li>
        </ul>
        <h2>Work Experience</h2>
        <ul>
            <li><strong>Associate Software Developer</strong>, Melody Mocktail, Hyderabad (Mar 2025 – Present)<br>
                Developed and maintained Django REST APIs for affiliate product integration. Ensured secure, scalable
                backend handling of product data and user actions.
            </li>
            <li><strong>Website Developer</strong>, Labnest Retail Services, Kolkata (Oct 2024 – Present)<br>
                Built and customized WordPress site showcasing lab equipment. Managed content, design, and SEO for
                improved visibility.
            </li>
            <li><strong>Data Analyst</strong>, Assurex e-Consultant, Kolkata (Aug 2023 – Jan 2024)<br>
                Solved problems using Python, worked on ML tasks like data cleaning, model building, and evaluation.
            </li>
        </ul>
        <h2>Projects</h2>
        <ul>
            <li><strong>Django REST API for Dynamic Redirect Management:</strong> CRUD operations, image upload,
                filtering, sorting, and unit testing. <a
                    href="https://github.com/laxmanchandrarana/Django-Backend-Assignment-Melody-Mocktail"
                    target="_blank">GitHub</a></li>
            <li><strong>File Manager Application:</strong> Python app with Tkinter for file organizing. <a
                    href="https://github.com/laxmanchandrarana/File-Manager-Application-with-built-in-File-Organizer.git"
                    target="_blank">GitHub</a></li>
            <li><strong>Google Assistant Controlled Home Automation:</strong> Voice control via ESP8266 microcontroller
                (IoT).</li>
            <li><strong>Lab Equipment Website:</strong> WordPress site built for Labnest.in. <a
                    href="https://labnest.in/" target="_blank">Labnest</a></li>
            <li><strong>Astrology Website:</strong> Built with HTML and CSS for CelebrityAstrologer. <a
                    href="https://celebrityastrologer.in/" target="_blank">Website</a></li>
        </ul>
    </div>
</body>
</html>
"""


soup = BeautifulSoup(html_content, 'html.parser')

# Extract Skills
skills_section = soup.find('h2', text='Technical Skills').find_next_sibling('ul')
if skills_section:
    for item in skills_section.find_all('li'):
        skill_name = item.strong.text.rstrip(':') if item.strong else "Unknown Skill"
        skill_desc = item.text.split(':', 1)[1].strip() if ':' in item.text else "No Description"
        
        Skill.objects.create(name=skill_name, description=skill_desc)

# Extract Education (using dummy data since the HTML does not have a clear section for this)
Education.objects.create(institution="Gopalpur Deshbandhu Chittaranjan High School", degree="Class X", year=2017)
Education.objects.create(institution="Gopalpur Deshbandhu Chittaranjan High School", degree="Class XII (Science)", year=2019)
Education.objects.create(institution="JIS College of Engineering", degree="B.Tech ECE", year=2023)

# Extract Projects
projects_section = soup.find('h2', text='Projects').find_next_sibling('ul')
if projects_section:
    for item in projects_section.find_all('li'):
        title = item.text.split(':')[0].strip()
        description = item.text.split(':')[1].split('GitHub')[0].strip()
        link = item.find('a')['href'] if item.find('a') else None
        Project.objects.create(title=title, description=description, link=link)


print("Database populated successfully!")
		<!-- Mobile Specific Meta -->
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="p:domain_verify" content="e72a2ddcc435d08a0c909b466969f6e2"/>
		<!--Css Fils -->
		<link rel="stylesheet" href="./assets/animate.css">
		<link rel="stylesheet" href="./assets/flaticon-31.css">
		
		<link rel="stylesheet" href="./assets/owl.carousel.css">
		<link rel="stylesheet" href="./assets/typer.css">
		<link rel="stylesheet" href="./assets/slick-theme.css">
		<link rel="stylesheet" href="./assets/slick.css">
		<link rel="stylesheet" href="./assets/bootstrap.min.css">
		<link rel="stylesheet" href="./assets/style-31.css">
		
		<script src="https://kit.fontawesome.com/d59710d54e.js" crossorigin="anonymous"></script>

	<style type="text/css">@font-face { font-family: Roboto; src: url("chrome-extension://mcgbeeipkmelnpldkobichboakdfaeon/css/Roboto-Regular.ttf"); }</style></head>

	<body class="apihu-port-body" data-new-gr-c-s-check-loaded="14.1062.0" data-gr-ext-installed="">

		<div class="apihu-port-body-overlay"></div>

		<!-- Preloader-->
		<div class="loading-preloader" style="display: none;">
			<div id="loading-preloader">
				<div class="line_shape"></div>
				<div class="line_shape"></div>
				<div class="line_shape"></div>
				<div class="line_shape"></div>
				<div class="line_shape"></div>
				<div class="line_shape"></div>
				<div class="line_shape"></div>
				<div class="line_shape"></div>
				<div class="line_shape"></div>
				<div class="line_shape"></div>
			</div>
		</div>
		<!-- Preloader End -->

		<!-- ScrollTop Button -->
        <a href="#" class="apihu-port-scroll-top" style="display: none;"><i class="fas fa-chevron-up"></i></a>

		<!-- Header Start -->
		<header class="apihu-port-header-area">
			<div class="container">
				<div class="row">
					<div class="col-xl-2 col-lg-2 col-md-2 col-3">
						<div class="apihu-port-logo">
							<img src="./assets/lcr.png" alt="SaaSio Portfolio">
						</div>
					</div>
					<div class="col-xl-8 d-none d-lg-block text-center col-lg-8">
						<div class="apihu-port-main-navigation">
							<ul>
								<li><a href="#">Home</a></li>
								<li><a href="#apihu-port-resume">About</a></li>
								<li><a href="#apihu-port-feature">Projects</a></li>
								<li><a href="#apihu-port-pricing-area">Qualifications</a></li>
								<li><a href="#contact-details">Contact</a></li>
								
							</ul>
						</div>
					</div>
					<div class="col-xl-2 col-lg-2 col-md-10 col-9 text-right">
						<div class="apihu-port-header-cta">
							<a href="https://www.instagram.com/laxmanchandrarana/">Let's Chat <i class="fas fa-comment-dots"></i></a>
						</div>

						<div class="apihu-port-mobile-menu-hamburger">
							<a href="#"><i class="fas fa-bars"></i></a>
						</div>
					</div>
				</div>
			</div>
		</header>
		<!-- Header End -->

		<!-- Mobile Menu -->
		<div class="apihu-port-mobile-menu">
			<a href="#" class="apihu-port-menu-close"><i class="fas fa-times"></i></a>
			<a href="#" class="apihu-port-logo-wrapper"><img src="./assets/white-logo.png" alt=""></a>
			<ul>
								<li><a href="#">Home</a></li>
								<li><a href="#apihu-port-resume">About</a></li>
								<li><a href="#apihu-port-feature">Projects</a></li>
								<li><a href="#apihu-port-pricing-area">Qualifications</a></li>
								<li><a href="#contact-details">Contact</a></li>
			</ul>
		</div>
		<!-- Mobile Menu End -->

		<!-- Hero Start -->
		
		<section class="apihu-port-hero-area" id="apihu-port-hero">

			<!-- Hero bg shape -->
			
			<img class="apihu-port-hero-shape-1" src="./assets/hero-shape.png" alt="Shape">
			<img class="apihu-port-hero-shape-2" src="./assets/python.png" alt="Shape">
			<img class="apihu-port-hero-shape-3" src="./assets/arduino.png" alt="Shape">
			<img class="apihu-port-hero-shape-4" src="./assets/html.png" alt="Shape">
			<img class="apihu-port-hero-shape-5" src="./assets/sql.png" alt="Shape">
				
			
			
			<span class="apihu-port-hero-side-style-text">Laxman</span>
			<div class="container">
				<div class="row">
					<div class="col-xl-8 col-lg-8">
						<div class="apihu-port-hero-left">
							<p class="apihu-port-hero-subtitle wow slideInDown" style="visibility: visible; animation-name: slideInDown;">Welcome to My World</p>
							<h1 class="apihu-port-hero-title cd-headline clip is-full-width">Hi there!<br>I’m Laxman Chandra Rana<span class="apihu-port-hero-title-color cd-words-wrapper" style="width: 67.5582px; overflow: hidden;">
							</span>
								<span class="apihu-port-hero-title-small-text"><div class="type">
    <p>I'm into <span class="typed-text"></span><span class="cursor">&nbsp;</span></p>
  </div></span> 
							</h1>
							
							<ul class="apihu-port-hero-btn-wrap wow slideInUp" style="visibility: visible; animation-name: slideInUp;">
								<li><a class="apihu-port-primary-btn apihu-port-hero-btn-gradient" href="mailto:laxmanchandrarana2000@gmail.com">Contact Me +</a></li>
								<li><a class="apihu-port-secondary-btn apihu-port-hero-btn-white" href="#apihu-port-resume">About Me <i class="fa-solid fa-arrow-down"></i></a></li>
							</ul>
						</div>
					</div>
					<div class="col-xl-4 col-lg-4">
						<!-- hero area social -->
						<div class="apihu-port-hero-social">
							<ul>
								<li><a href="https://www.linkedin.com/in/laxmanchrana/"><i class="fa-brands fa-linkedin-in"></i></a></li>
								<li><a href="https://github.com/laxmanchandrarana"><i class="fa-brands fa-github"></i></a></li>
								<li><a href="https://www.instagram.com/laxmanchandrarana/"><i class="fab fa-instagram"></i></a></li>
							</ul>
						</div>
						<div class="apihu-port-hero-right wow slideInRight" style="visibility: visible; animation-name: slideInRight;">
							<div class="apihu-port-hero-right-img">
								<img src="./assets/landing_image.png" alt="Hero Area">
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
		<!-- Hero End -->

		<!-- About Start -->
		<section class="apihu-port-about-area" id="apihu-port-resume">
			<img src="./assets/about-shape-1.png" alt="" class="apihu-port-about-shape">

			<div class="container">
				<div class="row">
					<div class="col-xl-6 col-lg-6">
						<div class="apihu-port-about-left wow slideInLeft" style="visibility: visible; animation-name: slideInLeft;">
							<div class="apihu-port-about-img">
								<img src="./assets/left_python.png" alt="">
							</div>
						</div>
					</div>
					<div class="col-xl-6 col-lg-6">
						<div class="apihu-port-about-right">
							<h3 class="apihu-port-about-subtitle">About Laxman</h3>
							<h2 class="apihu-port-about-title">Passionate about new tech. and <span>Python</span>.</h2>
							<p class="apihu-port-about-text">I am a <b>B.Tech</b> graduate in <b>Electronics and Communication Engineering</b> with a
								passion for technology and innovation. My academic journey has been marked
								by hands-on experience in <b>Python programming</b> and <b>Internet of Things (IoT)</b>
								projects. I have also ventured into the research domain, contributing to the field
								with a publication titled <b>"A Novel Method of CCTV Video Compression using
									Down Sampling"</b>.
								Professionally, I have served as an <b>Academic Research Associate</b> at <b>Assurex EConsultant</b> from <b>August</b> to <b>December</b> of <b>2023</b>, a role centered on <b>Academic
									Software Development</b>. Also, I undertook an <b>internship</b> as a <b>Desktop App
										Developer</b> at <b>The Bengal Studio</b> in <b>August, 2023</b>. This role provided me with
								hands-on experience in designing and implementing software applications.</p>
							<div class="apihu-port-about-expertise">
								<ul class="nav nav-pills" id="pills-tab" role="tablist">
									<li class="nav-item">
									  <a class="nav-link active show" id="pills-home-tab" href="https://www.linkedin.com/in/laxmanchrana/" role="tab" aria-controls="pills-home" aria-selected="true"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
									</li>
									<li class="nav-item">
									  <a class="nav-link active show" id="pills-profile-tab" href="https://github.com/laxmanchandrarana" role="tab" aria-controls="pills-profile" aria-selected="false"><i class="fa-brands fa-square-github"></i> Github</a>
									</li>
									
								  </ul>
							
								  <div class="tab-content" id="pills-tabContent">
										<div class="tab-pane fade active show" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">
											<ul>
												<li>
													<span class="apihu-port-expertise-title">Worked with Tkinter, OS, PyGame, NumPy, Pandas </span>
													<span class="apihu-port-expertise-text">Useful Libraries in Python</span>
												</li>
												<li>
													<span class="apihu-port-expertise-title">Currently working with <font style="color: blue;">Web Development</font></span>
													<span class="apihu-port-expertise-text">Soon going to gain some experience in it.</span>
												</li>
												<li>
													<span class="apihu-port-expertise-title">I am into Academic Technical content creation and Software Development .</span>
													<span class="apihu-port-expertise-text">Having experience about 6 months+.</span>
													<!-- <span class="apihu-port-expertise-text">Check out my blogging site: <a href="https://foxstack.blogspot.com/" style="text-decoration: none; color: #e70820;">FoxStack</a></span> -->
												</li>
											</ul>
										</div>
										
							<div class="apihu-port-about-btn">
								<a href="https://drive.google.com/file/d/1UKr62RZJpQX7NlTDqtj6kON4bvMZhNGL/view?usp=sharing">Download CV <i class="fas fa-download"></i></a>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
		<!-- About End -->

		<!-- Service Start -->
		<section class="apihu-port-service-area" id="apihu-port-feature">
			<img class="apihu-port-service-shape-1" src="./assets/service-shape-1.png" alt="Service Shape">
			<img class="apihu-port-service-shape-2" src="./assets/service-shape-2.png" alt="Service Shape">

			<div class="container">
				<div class="row">
					<div class="col-xl-12 text-center">
						<div class="apihu-port-section-heading">
							<p class="apihu-port-section-subtitle">Trying to make this section powerful and inspiring.</p>
							<h2 class="apihu-port-section-title">Projects and <span class="apihu-port-section-title-color">Achievements</span>.</h2>
						</div>
					</div>
				</div>

				<div class="row">
					<div class="col-xl-3 col-lg-3 col-md-6">
						<div class="apihu-port-single-service wow fadeInUp" data-wow-delay="0.2s" style="visibility: visible; animation-delay: 0.2s; animation-name: fadeInUp;">
							<div class="apihu-port-service-icon-box">
								<i class="fa-solid fa-chart-bar"></i>
							</div>
							<h3 class="apihu-port-single-service-title">Astrology Website using HTML and CSS</h3>
							<p class="apihu-port-single-service-text">Developed a responsive and user-friendly website for **Celebrity Astrologer**, incorporating a professional design with seamless astrology content integration. Optimized for fast loading times, mobile responsiveness, and intuitive navigation, ensuring an enhanced user experience. The site is designed to deliver engaging astrology services and content efficiently across all devices. 
								</p>
							<a class="apihu-port-single-service-btn" href="https://celebrityastrologer.in/" target="_blank">Visit site <i class="fas fa-plus"></i></a>
						</div>
					</div>
					<div class="col-xl-3 col-lg-3 col-md-6">
						<div class="apihu-port-single-service wow fadeInUp" data-wow-delay="0.2s" style="visibility: visible; animation-delay: 0.2s; animation-name: fadeInUp;">
							<div class="apihu-port-service-icon-box">
								<i class="fa-solid fa-chart-bar"></i>
							</div>
							<h3 class="apihu-port-single-service-title">File Manager Application with built-in File Organizer using Python</h3>
							<p class="apihu-port-single-service-text">This  is  a  unique  file  manager  application  that  has  a function  or  button  in  it  called  Organizer.  This  function helps  you  nicely  organize  your  files.  This  project  wasmade  using  the  'tkinter'  and  'OS'  modules  of  Python.When you run this project, you can go through your local disks. Locate to a folder that you want to organize. Afterpressing  the  “Organize  ”  button  in  the  application,  the program will separate all your different files into different folders, like 'Audio' files in the 'AudioFiles' folder. 
								</p>
							<a class="apihu-port-single-service-btn" href="https://github.com/laxmanchandrarana/File-Manager-Application-with-built-in-File-Organizer" target="_blank">Read More <i class="fas fa-plus"></i></a>
						</div>
					</div>
					<div class="col-xl-3 col-lg-3 col-md-6">
						<div class="apihu-port-single-service wow fadeInUp" data-wow-delay="0.4s" style="visibility: visible; animation-delay: 0.4s; animation-name: fadeInUp;">
							<div class="apihu-port-service-icon-box">
								<i class="fa-solid fa-robot"></i>
							</div>
							<h3 class="apihu-port-single-service-title">Google Assistant Controlled Home Automation</h3>
							<p class="apihu-port-single-service-text">In this home automation, as the user gives commands tothe  Google  assistant,  Home  appliances  like  Bulb,  Fan and  Motor  etc.,  can  be  controlled  accordingly.  The commands  given  through  the  Google  assistant  are decoded  and  then  sent  to  the  microcontroller,  the microcontroller in turn controls the relays connected toit. The device connected to the respective relay can beturned On or OFF as per the users request to the Google Assistant. The microcontroller used id ESP8266 and thecommunication  between  the  microcontroller  and  the application is established via Wi-Fi (Internet).
								</p>
							<!-- <a class="apihu-port-single-service-btn" href="#">Read More <i class="fas fa-plus"></i></a> -->
						</div>
					</div>
					<div class="col-xl-3 col-lg-3 col-md-6">
						<div class="apihu-port-single-service wow fadeInUp" data-wow-delay="0.6s" style="visibility: visible; animation-delay: 0.6s; animation-name: fadeInUp;">
							<div class="apihu-port-service-icon-box">
								<i class="fa-solid fa-paintbrush"></i>
							</div>
							<h3 class="apihu-port-single-service-title">Text Editor using Python</h3>
							<p class="apihu-port-single-service-text">
								This  project  was  made  using  'tkinter'  and  'OS'module of Python.In this application you can write text  and  also  you  can  change  the  font  type,font colour,font size and bold,italic,underline the text.</p>
							<a class="apihu-port-single-service-btn" href="https://github.com/laxmanchandrarana/Text-Editor" target="_blank">Read More <i class="fas fa-plus"></i></a>
						</div>
					</div>
					<!-- <div class="col-xl-3 col-lg-3 col-md-6">
						<div class="apihu-port-single-service wow fadeInUp" data-wow-delay="0.8s" style="visibility: visible; animation-delay: 0.8s; animation-name: fadeInUp;">
							<div class="apihu-port-service-icon-box">
								<i class="fa-solid fa-code-merge"></i>
							</div>
							<h3 class="apihu-port-single-service-title">Hacktober Fest</h3>
							<p class="apihu-port-single-service-text">Completed HactoberFest with acceptance of 4+ PR on GitHub. </p>
							<a class="apihu-port-single-service-btn" href="#">Read More <i class="fas fa-plus"></i></a>
						</div>
					</div> -->
				</div>
				<div class="row">
					<div class="col-xl-12 text-center">
						<div class="apihu-port-service-load-more-btn">
							<!-- <a href="#">Load More <i class="fas fa-plus"></i></a> -->
						</div>
					</div>
				</div>
			</div>
		</section>
		<!-- Service End -->

		<!-- CTA Start -->
		<section class="apihu-port-cta-area">
			<img class="apihu-port-cta-shape" src="./assets/cta-bg.png" alt="Cta shape">

			<div class="container">
				<div class="row">
					<div class="col-xl-12">
						<div class="apihu-port-cta-content-wrap">

							<img class="apihu-port-cta-container-shape" src="./assets/cta-bg-shape.png" alt="Cta container shape">

							<div class="row">
								<div class="col-xl-8 col-lg-8">
									<div class="apihu-port-cta-content-text">
										<p>Get It Touch</p>
										<h2>Have a Project on Your Mind</h2>
										<a href="#contact-details">Contact Me +</a>
									</div>
								</div>
								<div class="col-xl-4 col-lg-4">
									<div class="apihu-port-cta-content-img">
										<!-- <img src="./assets/cta-right.png" alt="Call to action area"> -->
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
		<!-- CTA End -->

		<!-- Pricing Start -->
		<section class="apihu-port-pricing-area" id="apihu-port-pricing-area">
			<img class="apihu-port-pricing-shape-left" src="./assets/pricing-left-shape.png" alt="Pricing Area Shape left">
			<img class="apihu-port-pricing-shape-right" src="./assets/pricing-right-shape.png" alt="Pricing Area Shape right">

			<div class="container">
				<div class="row">
					<div class="col-xl-12 text-center">
						<div class="apihu-port-section-heading">
							<p class="apihu-port-section-subtitle">Qualifications</p>
							<h2 class="apihu-port-section-title">Academic and Professional</h2>
							<p class="apihu-port-section-text">
								
							</p>
						</div>
					</div>
				</div>

				<div class="row">
					<div class="col-xl-4 col-lg-4 col-md-6">
						<div class="apihu-port-single-pricing wow fadeInUp" data-wow-delay="0.2s" style="visibility: visible; animation-delay: 0.2s; animation-name: fadeInUp;">
							<h3>Class X</h3>
							<h4>Gopalpur Deshbandhu Chittaranjan High School</h4>
							<ul>
								<li><i class="fa-solid fa-location-pin"></i> Gopalpur, Paschim Madinipur, 721212</li>
								<!-- <li><i class="fa-solid fa-percent"></i> Aggregate: 96.8</li> -->
								<!-- <li><img src="./assets/ais.png" alt="ais_img"></li> -->
							</ul>
							<a>
								Completed in 2017<i class="fa-solid fa-check"></i>
							</a>
						</div>
					</div>
					
					<div class="col-xl-4 col-lg-4 col-md-6">
						<div class="apihu-port-single-pricing wow fadeInUp" data-wow-delay="0.2s" style="visibility: visible; animation-delay: 0.2s; animation-name: fadeInUp;">
							<h3>Class XII (Science)</h3>
							<h4>Gopalpur Deshbandhu Chittaranjan High School</h4>
							<ul>
								<li><i class="fa-solid fa-location-pin"></i> Gopalpur, Paschim Madinipur, 721212</li>
								<!-- <li><i class="fa-solid fa-percent"></i> Aggregate: 96.8</li> -->
								<!-- <li><img src="./assets/ais.png" alt="ais_img"></li> -->
							</ul>
							<a>
								Completed in 2019<i class="fa-solid fa-check"></i>
							</a>
						</div>
					</div>
					
					<div class="col-xl-4 col-lg-4 col-md-6">
						<div class="apihu-port-single-pricing wow fadeInUp" data-wow-delay="0.2s" style="visibility: visible; animation-delay: 0.2s; animation-name: fadeInUp;">
							<h3>B.Tech ECE</h3>
							<h4>JIS College of <br>Engineering</h4>
							<ul>
								<li><i class="fa-solid fa-location-pin"></i> Kalyani, Nadia, 741235</li>
								<li>Overall CGPA: 8.68</li>
								<!-- <li><img src="./assets/jis.png" alt="ais_img"></li> -->
							</ul>
							<a>
								Completed in 2023 <i class="fa-solid fa-check"></i>
							</a>
						</div>
					</div>
					
				</div>
			</div>
		</section>
		<!-- Pricing End -->

		
		<!-- Contact Start -->
		<section class="apihu-port-contact-area" id="contact-details">
			<div class="container">
				<div class="row">
					<div class="col-xl-6 col-lg-6 text-left">
						<div class="apihu-port-section-heading">
							<p class="apihu-port-section-subtitle">Contact Me</p>
							<h2 class="apihu-port-section-title">Get in Touch With Me</h2>
						</div>
					</div>
					
				</div>

				<div class="row">
					
					<div class="col-xl-6">
						<div class="apihu-port-contact-right">
							<div class="apihu-port-contact-right-img">
								<img src="./assets/contact-illust.png" alt="Contact Right">
							</div>
							<div class="apihu-port-contact-right-content">
								
								<div class="apihu-port-contact-text">
									<span class="apihu-port-contact-number"><a href="mailto:laxmanchandrarana2000@gmail.com">MailTo: <font style="font-weight: bold; color: #e70280;">laxmanchandrarana2000@gmail.com</font></a></span>
									<span class="apihu-port-contact-email"><a href="https://www.linkedin.com/in/laxmanchrana/">DM on LinkedIn: <font style="font-weight: bold; color: #e70280;">laxmanchrana</font></a></span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
		<!-- Contact End -->
		
		
		

		<!-- Footer Start -->
		<!-- Site footer -->
    <footer class="site-footer">
      <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-6">
            <img src="./assets/lcr_footer.png" alt="footer logo">
            <p class="text-justify">Thank you for visiting my personal portfolio site. I would really be glad to connect with you. Message me on my LinkedIn handle or on my Instagram handle.</p><p>Keep learning and keep rising.</p>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>Contact Info</h6>
            <ul class="footer-links">
              <li><i class="fa-solid fa-phone" style="color: yellow;"></i>  +91 8167749719</li>
              <li><i class="fa-solid fa-envelope" style="color: yellow;"></i>  laxmanchandrarana2000@gmail.com</li>
              <li><i class="fa-solid fa-location-pin" style="color: yellow;"></i>  Kolkata, W.B., India</li>
            </ul>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>Quick Links</h6>
            <ul class="footer-links">
              <li><a href="#">Home</a></li>
								<li><a href="#apihu-port-resume">About</a></li>
								<li><a href="#apihu-port-feature">Projects</a></li>
								<li><a href="#apihu-port-pricing-area">Qualifications</a></li>
								<li><a href="#contact-details">Contact</a></li
            </ul>
          </div>
        </div>
        <hr>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-8 col-sm-6 col-xs-12">
            <p class="copyright-text">Designed with <i class="fa fa-heart pulse" style="color: #e90606;"></i> by
         <a href="https://www.linkedin.com/in/laxmanchrana/">Laxman Chandra Rana</a>.
            </p>
          </div>

          <div class="col-md-4 col-sm-6 col-xs-12">
            <ul class="social-icons">
              <li><a class="github" href="https://github.com/laxmanchandrarana"><i class="fa fa-github"></i></a></li>
              <li><a class="instagram" href="https://www.instagram.com/laxmanchandrarana/"><i class="fa fa-instagram"></i></a></li>
              <li><a class="linkedin" href="https://www.linkedin.com/in/laxmanchrana//"><i class="fa fa-linkedin"></i></a></li>   
            </ul>
          </div>
        </div>
      </div>
</footer>
		<!-- Footer End -->

        <!-- For Js Library -->
		<script src="./assets/jquery.js.download"></script>
		<script src="./assets/bootstrap.min.js.download"></script>
		<script src="./assets/owl.js.download"></script>
		<script src="./assets/slick.js.download"></script>
		<script src="./assets/waypoints.min.js.download"></script>
		<script src="./assets/wow.min.js.download"></script>
		<script src="./assets/isotope.pkgd.js.download"></script>
		<script src="./assets/typer-new.js.download"></script>
		<script src="./assets/appear.js.download"></script>
		<script src="./assets/progress-bar.js.download"></script>
		<script src="./assets/scripts-31.js.download"></script>

		<script src="./assets/type.js"></script>
		

	
		
                                                           <div id="imageDownloaderSidebarContainer"><div class="image-downloader-ext-container"><div tabindex="-1" class="b-sidebar-outer"><!----><div id="image-downloader-sidebar" tabindex="-1" role="dialog" aria-modal="false" aria-hidden="true" class="b-sidebar shadow b-sidebar-right bg-light text-dark" style="width: 500px; display: none;"><!----><div class="b-sidebar-body"><div></div></div><!----></div><!----><!----></div></div></div>
<div class="container">
  
<h2>About Me</h2>
<p>I am Laxman Chandra Rana, a full-time Associate Software Developer with strong backend development experience in Django REST APIs and full-stack exposure using WordPress. My projects span web development, automation, and Python-based desktop tools. I value clean architecture, testable code, and continuous learning.</p>

  
<h2>Technical Skills</h2>
<ul>
  <li><strong>Languages:</strong> Python, HTML, CSS, Embedded C</li>
  <li><strong>Libraries & Tools:</strong> Django, Docker, Postman, Tkinter, Celery, Jira Board, BitBucket, OS, Pandas, Git, Github, Wordpress, ODOO</li>
  <li><strong>Database:</strong> MySQL, Postgres</li>
  <li><strong>Languages Known:</strong> English, Hindi, Bengali</li>
</ul>

  
<h2>Work Experience</h2>
<ul>
  <li><strong>Associate Software Developer</strong>, Melody Mocktail, Hyderabad (Mar 2025 – Present)<br>
      Developed and maintained Django REST APIs for affiliate product integration. Ensured secure, scalable backend handling of product data and user actions.
  </li>
  <li><strong>Website Developer</strong>, Labnest Retail Services, Kolkata (Oct 2024 – Present)<br>
      Built and customized WordPress site showcasing lab equipment. Managed content, design, and SEO for improved visibility.
  </li>
  <li><strong>Data Analyst</strong>, Assurex e-Consultant, Kolkata (Aug 2023 – Jan 2024)<br>
      Solved problems using Python, worked on ML tasks like data cleaning, model building, and evaluation.
  </li>
</ul>

  
<h2>Projects</h2>
<ul>
  <li><strong>Django REST API for Dynamic Redirect Management:</strong> CRUD operations, image upload, filtering, sorting, and unit testing. <a href="https://github.com/laxmanchandrarana/Django-Backend-Assignment-Melody-Mocktail" target="_blank">GitHub</a></li>
  <li><strong>File Manager Application:</strong> Python app with Tkinter for file organizing. <a href="https://github.com/laxmanchandrarana/File-Manager-Application-with-built-in-File-Organizer.git" target="_blank">GitHub</a></li>
  <li><strong>Google Assistant Controlled Home Automation:</strong> Voice control via ESP8266 microcontroller (IoT).</li>
  <li><strong>Lab Equipment Website:</strong> WordPress site built for Labnest.in. <a href="https://labnest.in/" target="_blank">Labnest</a></li>
  <li><strong>Astrology Website:</strong> Built with HTML and CSS for CelebrityAstrologer. <a href="https://celebrityastrologer.in/" target="_blank">Website</a></li>
</ul>

  