# News Recommendation App with Vespa (All-in-One Notebook)

This project demonstrates how to build a comprehensive news recommendation application using Vespa, entirely within a single Python notebook. This guide covers everything from basic search functionality to advanced recommendation techniques, leveraging embeddings and dynamic popularity signals.

## 🎯 Project Overview

This series is a simplified version of Vespa's [News search and recommendation tutorial](https://blog.vespa.ai/build-news-search-app-from-python-with-vespa/), adapted to be run conveniently in a single notebook. We'll use a demo version of the [Microsoft News Dataset (MIND)](https://msnews.github.io/) to allow anyone to follow along locally.

## 🚀 What You'll Learn

The notebook will walk you through:

1. **Setting up a Basic Search Application**: Learn how to define schemas, add fields, and perform keyword, attribute, and grouped searches.

2. **Implementing News Recommendation with Embeddings**: Discover how to integrate user and news article embeddings for approximate nearest neighbor (ANN) search, enabling personalized recommendations.

3. **Enhancing Recommendations with Dynamic Popularity**: Understand how to incorporate real-time popularity signals (like click-through rates) into the ranking process using parent-child relationships in Vespa.

By the end of this notebook, you'll have a functional news recommendation system built and deployed locally with Vespa.

## 📋 Prerequisites

To run this notebook, you'll need:

### Required Software
- **Docker**: Vespa runs in Docker containers for local deployment
  - [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
  - Ensure Docker is running before starting the notebook

- **Python 3 (latest)**: Required for running the notebook and dependencies

### Required Python Packages
Install the necessary packages using pip:

```bash
pip install pyvespa pandas numpy requests jupyter
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd News_Recommendation_Vespa
```

### 2. Start Docker
Make sure Docker Desktop is running on your system.

### 3. Launch Jupyter Notebook
```bash
jupyter notebook news_recommeder.ipynb
```

### 4. Run the Notebook
The notebook will handle:
- Downloading the necessary dataset automatically
- Setting up the Vespa application
- Guiding you through each step of development and deployment

## 📁 Project Structure

```
News_Recommendation_Vespa/
├── news_recommeder.ipynb    # Main notebook with complete tutorial
├── README.md               # This file
├── requirements.txt        # Python dependencies
└── data/                  # Dataset files (auto-downloaded)
```

## 🔧 Features Implemented

### Basic Search Functionality
- **Keyword Search**: Full-text search across news articles
- **Attribute Filtering**: Filter by date, category, and other metadata
- **Grouped Search**: Aggregate results by categories or sources

### Advanced Recommendation System
- **User Embeddings**: Personalized recommendations based on user behavior
- **Content Embeddings**: Semantic similarity between articles
- **ANN Search**: Fast approximate nearest neighbor search for scalability
- **Hybrid Ranking**: Combine multiple signals for optimal recommendations

### Dynamic Popularity Integration
- **Real-time CTR**: Click-through rate tracking and integration
- **Parent-Child Relationships**: Efficient popularity signal updates
- **Time-decay Functions**: Recent popularity weighted higher

## 📊 Dataset Information

This project uses a demo version of the Microsoft News Dataset (MIND), which includes:
- **News Articles**: Title, abstract, category, and content
- **User Interactions**: Click history and behavior patterns
- **Embeddings**: Pre-computed user and article embeddings
- **Date Range**: Typically covers November 2019 data

## 🚨 Troubleshooting

### Common Issues

**Docker Connection Error**
```
DockerException: Error while fetching server API version
```
**Solution**: Ensure Docker Desktop is running and accessible.

**Memory Issues**
If you encounter memory problems, try:
- Reducing batch sizes in the notebook
- Limiting the dataset size for testing
- Increasing Docker memory allocation

**Port Conflicts**
If Vespa ports are occupied:
- Stop other Vespa instances: `docker stop $(docker ps -q)`
- Use different ports in the VespaDocker configuration

## 📈 Performance Tips

- **Local Development**: Use smaller dataset samples for faster iteration
- **Production**: Consider Vespa Cloud for scalable deployment
- **Memory**: Allocate sufficient memory to Docker (8GB+ recommended)
- **CPU**: Multi-core systems will significantly improve indexing speed

## 🔗 Useful Resources

- [Vespa Documentation](https://docs.vespa.ai/)
- [PyVespa API Reference](https://pyvespa.readthedocs.io/)
- [MIND Dataset Paper](https://www.microsoft.com/en-us/research/publication/mind-a-large-scale-dataset-for-news-recommendation/)
- [Vespa News Tutorial](https://docs.vespa.ai/en/tutorials/news-search.html)

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs or issues
- Suggesting improvements
- Adding new features
- Improving documentation

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Vespa Team**: For the excellent search engine and documentation
- **Microsoft Research**: For providing the MIND dataset
- **Community**: For feedback and contributions

---

**Ready to dive in and build your own news recommender?** 🚀

Start by opening the `news_recommeder.ipynb` notebook and follow along with the step-by-step guide!


---
 
### 🌐 Connect with Me
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/isidharthrai/)
[![Website](https://img.shields.io/badge/-Portfolio-222?logo=google-chrome&style=flat-square)](https://www.sidharthrai.com/)
 
---