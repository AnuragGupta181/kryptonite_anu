# Kryptonite 🔥

A satellite-based fire detection system built with FastAPI and machine learning. This project provides real-time fire detection capabilities with geospatial mapping and data analysis.

## 🚀 Features

- **Fire Detection API**: RESTful API endpoints for fire detection and monitoring
- **Geospatial Mapping**: Interactive maps using Folium and GeoPandas
- **Machine Learning Pipeline**: Automated data ingestion, transformation, and model training
- **Real-time Processing**: FastAPI-based backend with CORS support
- **Regional Configuration**: Customizable region-based detection using YAML configuration

## 📋 Prerequisites

- Python 3.13+
- pip or uv package manager

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/VashuTheGreat/MultiRag.git
   cd Kryptonite
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or using uv:

   ```bash
   uv pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory with your configuration:

   ```env
   # Add your environment variables here
   ```

## 🚦 Usage

### Running the API Server

```bash
python main.py
```

The API will be available at `http://127.0.0.1:8002`

### API Endpoints

- **User Routes**: `/api/user/*`
- **Map Routes**: `/api/map/*`

## 📁 Project Structure

```
Kryptonite/
├── src/
│   ├── app.py                 # FastAPI application
│   ├── components/            # Data processing components
│   ├── configuration/         # Configuration management
│   ├── controllers/           # API controllers
│   ├── data_access/          # Data access layer
│   ├── entity/               # Data entities
│   ├── exception/            # Custom exceptions
│   ├── logger/               # Logging utilities
│   ├── pipeline/             # ML pipelines
│   ├── routes/               # API routes
│   └── utils/                # Utility functions
├── config/                   # YAML configuration files
│   ├── model.yaml
│   ├── region.yaml
│   └── schema.yaml
├── tests/                    # Unit tests
├── main.py                   # Application entry point
├── requirements.txt          # Python dependencies
└── pyproject.toml           # Project metadata
```

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

## 🔧 Configuration

The project uses YAML configuration files located in the `config/` directory:

- `model.yaml`: ML model configuration
- `region.yaml`: Regional settings for fire detection
- `schema.yaml`: Data schema definitions

## 📦 Key Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server
- **Ultralytics**: YOLO-based object detection
- **GeoPandas**: Geospatial data processing
- **Folium**: Interactive mapping
- **PyTorch**: Deep learning framework
- **Pandas**: Data manipulation
- **scikit-learn**: Machine learning utilities

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**VashuTheGreat**

## 🙏 Acknowledgments

- Built for the Kryptonite Hackathon
- Powered by FastAPI and modern ML frameworks

---

**Note**: This project is part of a hackathon submission for satellite-based fire detection systems.
