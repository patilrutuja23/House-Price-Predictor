# Deployment Guide

Choose the platform that works best for you:

## Option 1: Render (Recommended for Flask) ✅

### Pros
- Easy Flask deployment
- Free tier available
- No serverless cold start issues
- Best for persistent background tasks

### Steps
1. Push to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Create new "Web Service"
4. Connect your GitHub repo
5. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn --chdir server server:app --log-file -`
6. Deploy

See `README.md` for detailed steps.

---

## Option 2: Vercel (Serverless) ⚡

### Pros
- Free tier with generous limits
- Auto-scaling
- Fast deployment
- Good for stateless APIs

### Cons
- Serverless cold starts (initial request slower)
- Max 12 second execution timeout (Hobby plan)
- File system is temporary

### Steps

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy from project root:**
   ```bash
   vercel --prod
   ```

   Or via GitHub:
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New" → "Project"
   - Import your GitHub repo
   - Click "Deploy"

4. **Your app will be live at:** `https://your-project.vercel.app`

### Important Notes for Vercel

⚠️ **Known Limitations:**
- Model artifacts must be committed to repo (can't fetch dynamically)
- Execution limited to 12 seconds per request (usually fine for price prediction)
- Each request is stateless (model reloaded per request)

✅ **Our setup already handles this:**
- `vercel.json` configured
- `server.py` exports Flask app
- Model files committed to repo

---

## Option 3: Railway.app

### Pros
- Simple Flask deployment
- Good free tier
- Traditional server (not serverless)

### Steps
1. Push to GitHub
2. Go to [Railway.app](https://railway.app)
3. Click "Create Project"
4. Connect GitHub repo
5. Railway auto-detects Flask and deploys

Set environment variables if needed.

---

## Option 4: PythonAnywhere

### Pros
- Python-specific hosting
- Web-based console
- Good for learning

### Steps
1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload your code
3. Configure WSGI file
4. Set up domain

---

## Comparison Table

| Platform | Type | Cold Start | Cost | Ease |
|----------|------|-----------|------|------|
| **Render** | Traditional | None | Free | ⭐⭐⭐ |
| **Vercel** | Serverless | ~1-3s | Free | ⭐⭐⭐ |
| **Railway** | Traditional | None | Free | ⭐⭐⭐ |
| **PythonAnywhere** | Traditional | None | Paid | ⭐⭐ |

---

## Recommended Choice

**For this project: Use Render or Railway**

Why?
- Traditional server = better for ML models (no cold start delays)
- Flask deployment is straightforward
- Both have free tiers
- No execution timeouts

---

## Local Testing Before Deployment

Always test locally first:

```bash
# Terminal 1: Run server
cd server
python server.py

# Terminal 2: Test API
curl http://localhost:5000/api/get_location_names

# Browser: Visit
http://localhost:5000/
```

---

## Troubleshooting

### Vercel: "Module not found" error
- Ensure all dependencies are in `requirements.txt`
- Model files must be committed to repo (not in `.gitignore`)

### Render: "Locations not loading"
- Check Render logs: `render.com/dashboard` → select project → "Logs"
- Verify `/api/get_location_names` endpoint works

### Cold start takes too long
- Use Render or Railway instead of Vercel
- Both have warm servers

---

**Questions?** Check the main `README.md` for more details!
