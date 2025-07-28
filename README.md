replace the project structure with this 
Dark_TRACER_Early_Detection/
│
├── 📁 Dark_TRACER_Early_Detection/        # Main Django config and routing
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── 📁 Remote_User/                        # Handles user-side logic
│   ├── 📁 migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── 📁 Service_Provider/                   # Handles admin-side logic
│   ├── 📁 migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── 📁 Template/                           # Frontend HTML files and assets
│
│   ├── 📁 Ruser/                           # User-side templates
│   │   ├── design.html
│   │   ├── get_url_details.html
│   │   ├── login.html
│   │   ├── Predict_Detection_Type.html
│   │   ├── predict_form.html
│   │   ├── ratings.html
│   │   ├── Register1.html
│   │   └── ViewYourProfile.html
│   │
│   ├── 📁 Sprovider/                       # Admin-side templates
│   │   ├── charts.html
│   │   ├── charts1.html
│   │   ├── design1.html
│   │   ├── dislikeschart.html
│   │   ├── Download_Predicted_DataSets.html
│   │   ├── Find_Malware_Detection_Type_Ratio.html
│   │   ├── likeschart.html
│   │   ├── Predict_Malware_Detection_Type_Details.html
│   │   ├── serviceproviderlogin.html
│   │   ├── train_model.html
│   │   └── View_Remote_Users.html
│   │
│   └── 📁 images/                          # Static UI images
│       ├── bg.jpg
│       ├── Login.jpg
│       └── Register.jpg
│
├── 📁 Database/                           # DB helpers or raw data
│
├── Labeled_Data.csv                      # Cleaned/labeled dataset
├── Malware_Datasets.csv                  # Raw malware dataset
│
├── build.sh                              # Build or deploy script (optional)
├── manage.py                             # Django project manager
├── render.yaml.txt                       # Render platform config
├── requirements.txt.txt                  # Python dependency file
└── .gitignore                            # Git ignore rules
and my repository name is https://github.com/hari-chintaparthi/ShadowWatch

replace those and share any questions are there to replace
