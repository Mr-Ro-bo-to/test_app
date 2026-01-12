## Local Development
```bash
pip install -r requirements-local.txt
streamlit run app.py
```

## Deployment
Streamlit Cloud automatically uses `requirements.txt`
```

**Benefit:** 
- ✅ Never accidentally push the wrong file
- ✅ Clear documentation for others
- ✅ Both files committed to git

## My Recommendation

Use **Strategy 3**. Here's what to create:

### `webapp-hello/requirements-local.txt`
```
streamlit
-e ../core
```

### `webapp-hello/requirements.txt`
```
streamlit
myproject-core @ git+https://github.com/YOUR_USERNAME/myproject-core.git