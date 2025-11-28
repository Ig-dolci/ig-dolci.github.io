# Personal GitHub Pages Website

This is a personal website hosted on GitHub Pages.

## Setup Instructions

1. **Create a GitHub repository**
   - Go to GitHub and create a new repository named `yourusername.github.io` (replace `yourusername` with your actual GitHub username)
   - Make sure the repository is public

2. **Upload these files**
   - Upload `index.html` and `style.css` to the root of your repository
   - Commit the changes

3. **Enable GitHub Pages**
   - Go to your repository Settings
   - Scroll down to the "Pages" section
   - Under "Source", select the main branch
   - Click Save

4. **Access your site**
   - Your site will be available at `https://yourusername.github.io`
   - It may take a few minutes for the site to become available

## Customization

### Edit Content
- Open `index.html` and replace the placeholder text with your information:
  - Your name in the header and title
  - About section with your bio
  - Research interests
  - Publications
  - Contact information

### Change Colors
- Edit `style.css` to customize colors:
  - Header background: `.hero` gradient colors
  - Accent colors: `#667eea` and `#764ba2`
  - Text colors throughout

### Add Your Photo
1. Add an image file (e.g., `profile.jpg`) to the repository
2. In `index.html`, add to the hero or about section:
```html
<img src="profile.jpg" alt="Your Name" class="profile-photo">
```
3. Add styling in `style.css`:
```css
.profile-photo {
    width: 200px;
    border-radius: 50%;
    margin: 20px 0;
}
```

### Add More Sections
You can add sections for:
- CV/Resume download
- Projects with GitHub links
- Blog posts
- Teaching materials
- Conference presentations

## Optional: Use Jekyll
For a more advanced site with blog functionality, consider using Jekyll:
- Create a `_config.yml` file
- Use markdown for content
- Choose from many free themes

## Need Help?
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
