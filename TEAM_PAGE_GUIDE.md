# Team Page Setup Guide

## Overview

A professional "Meet the Team" page has been added to Sosa Services, featuring:
- Owner: Tex
- Lead Developer: Xyloo

## What's Been Added

### 1. New Files Created

- `web/templates/team.html` - Team page template
- `web/static/css/team.css` - Team page styling
- `web/backend/team.py` - Team page route handler
- `web/static/images/team/` - Directory for team member photos

### 2. Modified Files

- `web/backend/app.py` - Added team route import
- `web/templates/base.html` - Added "Team" link to navigation
- `web/templates/index.html` - Added team preview section on homepage
- `web/static/css/index.css` - Added team preview styling

## Features

### Team Page (`/team`)

- Full profiles for Owner and Developer
- Professional bios and descriptions
- Skills showcase (for developer)
- Statistics display (for owner)
- Social media links
- Company values section
- Smooth animations and hover effects
- Fully responsive design

### Homepage Preview

- Quick team member cards
- Links to full team page
- Integrated into homepage flow

## Adding Team Member Photos

### Step 1: Prepare Images

Create or obtain profile photos for:
- `tex.png` - Owner photo
- `xyloo.png` - Developer photo

Recommended specifications:
- Format: PNG or JPG
- Size: 500x500 pixels minimum
- Aspect ratio: 1:1 (square)
- File size: Under 500KB
- Background: Transparent or solid color

### Step 2: Add Images

Place the images in:
```
web/static/images/team/
├── tex.png
└── xyloo.png
```

### Step 3: Fallback

If images are not provided, the default avatar will be used automatically.

## Customizing Team Information

### Owner (Tex) Information

Edit `web/templates/team.html` to customize:

**Bio Section:**
```html
<div class="team__member__bio">
    <p>Your custom bio paragraph 1...</p>
    <p>Your custom bio paragraph 2...</p>
</div>
```

**Statistics:**
```html
<div class="stat__item">
    <span class="stat__value">5+</span>
    <span class="stat__label">Years Experience</span>
</div>
```

**Social Links:**
```html
<button onclick="window.open('YOUR_TELEGRAM_URL', '_blank')" class="social-button telegram">
```

### Developer (Xyloo) Information

**Bio Section:**
Same as owner, edit the bio paragraphs

**Skills:**
```html
<div class="team__member__skills">
    <span class="skill__tag">Python</span>
    <span class="skill__tag">Flask</span>
    <!-- Add more skills -->
</div>
```

**Portfolio Link:**
Already set to: `https://xylooo.base44.app`

**Social Links:**
- Portfolio: `https://xylooo.base44.app`
- GitHub: `https://github.com/xyloo` (update if different)
- Telegram: `https://t.me/xyloo` (update if different)

## Customizing Company Values

Edit the values section in `web/templates/team.html`:

```html
<div class="value__item">
    <img src="icon.svg">
    <span class="value__title">Your Value Title</span>
    <span class="value__description">Your value description...</span>
</div>
```

Current values:
1. Quality First
2. Customer Focus
3. Privacy & Security
4. Innovation

## Styling Customization

### Colors

Edit `web/static/css/team.css`:

```css
.role.owner {
    background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
    color: #000;
}

.role.developer {
    background: linear-gradient(135deg, var(--accent) 0%, #00d4ff 100%);
    color: #000;
}
```

### Layout

Adjust spacing, sizes, and layout in `team.css`:
- `.team__member` - Main member card
- `.avatar__container.large` - Profile photo size
- `.team__member__header .name` - Name font size
- `.team__member__bio` - Bio text styling

## Navigation

The team page is accessible via:
1. Navigation bar: "Team" link
2. Homepage: "Learn More About Us" button in team preview section
3. Direct URL: `/team`

## Responsive Design

The team page is fully responsive:
- Desktop (1920px+): Full layout with side-by-side content
- Tablet (768px-1200px): Adjusted spacing
- Mobile (< 768px): Stacked layout, centered content

## Testing Checklist

- [ ] Team page loads at `/team`
- [ ] Navigation "Team" link works
- [ ] Homepage team preview displays
- [ ] "Learn More About Us" button redirects to `/team`
- [ ] Profile images display (or fallback to default)
- [ ] All social links work
- [ ] Responsive design works on mobile
- [ ] Hover effects work properly
- [ ] Animations trigger on scroll
- [ ] No console errors

## Social Media Links to Update

### Owner (Tex)
- Telegram: Update `https://t.me/tex` to actual username
- Discord: Update `https://discord.gg/sosaservices` to actual server

### Developer (Xyloo)
- Portfolio: `https://xylooo.base44.app` (already set)
- GitHub: Update `https://github.com/xyloo` if different
- Telegram: Update `https://t.me/xyloo` if different

## Adding More Team Members

To add additional team members:

1. Copy a team member block in `team.html`:
```html
<div class="team__member">
    <!-- Copy entire member structure -->
</div>
```

2. Add a divider between members:
```html
<div class="team__divider"></div>
```

3. Update information for new member

4. Add their photo to `web/static/images/team/`

5. Update homepage preview if desired

## SEO Optimization (Optional)

Add meta tags to `team.html`:

```html
{% block html %}
    <meta name="description" content="Meet the team behind Sosa Services - Tex (Owner) and Xyloo (Developer)">
    <meta name="keywords" content="Sosa Services team, about us, Tex, Xyloo">
    <link rel="stylesheet" href="{{ dated_url_for('static', filename='css/team.css') }}">
{% endblock %}
```

## Troubleshooting

### Images Not Loading
- Check file names match exactly (case-sensitive)
- Verify files are in `web/static/images/team/`
- Clear browser cache
- Check file permissions

### Page Not Loading
- Verify `team.py` is imported in `app.py`
- Check for Python syntax errors
- Restart the Flask application

### Styling Issues
- Clear browser cache
- Check CSS file is linked in template
- Verify CSS variable definitions in `style.css`
- Check for conflicting styles

### Social Links Not Working
- Verify URLs are correct
- Check `onclick` attributes
- Test links in browser console

## Future Enhancements

Consider adding:
- Team member testimonials
- Work history timeline
- Certifications and achievements
- Video introductions
- Contact forms per team member
- Team blog or news section

## Maintenance

Regular updates:
- Keep bios current
- Update statistics
- Add new skills as learned
- Update social media links
- Refresh photos periodically
- Add new team members as hired

---

**Created:** February 2026
**Last Updated:** February 2026
**Status:** Ready for customization
