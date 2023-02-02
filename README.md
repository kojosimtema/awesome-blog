# awesome-blog
![Awesome Blog_No_Post_HomePage_Not_LoggedIn](https://user-images.githubusercontent.com/53656050/200134109-c1dda710-f832-4775-88df-abb5d770dd5e.png)

## About

- This application was developed as project whiles studying at [Altschool Africa](https://altschoolafrica.com/schools/engineering)

- It is a blog application where users can post thier articles or blogs

- A user can search for posts by title or writer

- Posts can be edited or deleted by the writer

- Posts are sorted by the most recent

- The top five (5) viewed posts are displayed on the side

- A user needs to create an account to be able to post a blog however, any one can view blogs that have been posted

- You can read more on how this application was built [here](https://kojosimtema.hashnode.dev/create-a-blog-app-using-flask)

## Update
After the first commit I updated this application. Below are the new things I added to the application
- Upload of post image. I was using static images for all posts that were created in the previous version. I have now added an option to allow users add an image to their post and be able to update it as well

- Upload of user profile picture. Just as the post images, I was using static images for all user profile pictures. This time around, I've made it posible for users to update thier profile by adding a profile picture and a background picture

- Reload form without clearing data. In the previous version of this application, anything there's an error in a form being filled by a user, the page reloads and display the error message. This cleared all the information the user has filled in the form, hence they have to refill the form all over again. I have resolved this by making the form reload without clearing the form so that the user can continue from where they left off

## How to run this app

1. Create a virtual environment using your terminal
```
python -m venv your_environment_name
```

2. Activate virtual environment

Windows
```
source your_environment_name/Scripts/activate
```
linux/macOS
```
source your_environment_name/bin/activate
```

3. Install all Packages from requirements.txt file
```
pip install -r requirements.txt
```

4. Run the application
```
flask run
```
- if "flask run" does not work try..
```
python -m flask run
```

## Languages and Tools Used

<img align="center" src="https://user-images.githubusercontent.com/53656050/192115605-aebc5f03-6e81-4537-985a-6bdd7c95f83a.png" style="width:70px; height:70px" alt="python" /> <img align="center" src="https://user-images.githubusercontent.com/53656050/192116071-9fca6c24-67a8-439b-9bd3-07d859009a3c.png" style="width:70px; height:70px" alt="javascript" /> <img align="center" src="https://user-images.githubusercontent.com/53656050/192115449-02c26cf0-a2aa-4b45-a5ef-0243ac26f200.png" style="width:70px; height:70px" alt="flask" /> <img align="center" src="https://user-images.githubusercontent.com/53656050/192116146-e0492e46-c9fe-4155-831d-f88edcc98182.png" style="width:140px; height:70px" alt="html-css" /> <img align="center" src="https://user-images.githubusercontent.com/53656050/200135105-c334454b-e11a-48c0-87d6-35c25ec8691a.png" style="width:140px; height:70px" alt="html-css" />

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML
- CSS
- Tailwind CSS


## Screenshots

### *Homepage with no posts*

![Awesome Blog_No_post_HomePage_LoggedIn](https://user-images.githubusercontent.com/53656050/200135224-e3e3b6a1-5b80-4de3-872a-2a92ffd76db1.png)

### *Homepage with posts*

![Awesome Blog_Post_HomePage_LoggedIn](https://user-images.githubusercontent.com/53656050/200135226-d534c067-c9a8-439f-9a55-1b093c95cab5.png)

### *User Profile with no posts, viewed by user*

![Awesome Blog_Profile_No_Posts](https://user-images.githubusercontent.com/53656050/200135208-bb4099b3-cafd-436b-9bd8-42bfdf8a417c.png)

### *User Profile with posts*

![Profile_same_user_Awesome Blog](https://user-images.githubusercontent.com/53656050/211207306-0db6a145-4971-40ff-8788-4f5e402c9719.png)

## *User Profile viewed by others*

![Profile_Other_user_Awesome Blog](https://user-images.githubusercontent.com/53656050/211207342-68145414-2b6d-4762-bf50-32cbb9359292.png)


