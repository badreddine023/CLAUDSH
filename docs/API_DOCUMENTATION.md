# CLAUDSH API Documentation

This document provides comprehensive documentation for the CLAUDSH API, including endpoints, request/response formats, and usage examples.

## Base URL

```
http://localhost:5173/api
```

## Authentication

Currently, CLAUDSH uses OAuth-based authentication. Include your authentication token in the request headers:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## API Endpoints

### Quran Data Endpoints

#### Get Surah Information

Retrieve information about a specific surah (chapter).

**Request**
```
GET /api/quran/surah/:number
```

**Parameters**
- `number` (integer, required): Surah number (1-114)

**Response**
```json
{
  "number": 1,
  "name": "Al-Fatiha",
  "nameArabic": "الفاتحة",
  "revelation": "Meccan",
  "versesCount": 7,
  "juz": 1,
  "revelationOrder": 5,
  "verses": [
    {
      "number": 1,
      "arabic": "الحمد لله رب العالمين",
      "english": "All praise is due to Allah, the Lord of all worlds",
      "words": [...]
    }
  ]
}
```

#### Search Words

Search for words across the Quranic corpus.

**Request**
```
GET /api/quran/search?q=الحمد&limit=10
```

**Parameters**
- `q` (string, required): Search query (Arabic or English)
- `limit` (integer, optional): Maximum results (default: 10)
- `offset` (integer, optional): Result offset for pagination

**Response**
```json
{
  "total": 157,
  "results": [
    {
      "word": "الحمد",
      "surah": 1,
      "verse": 1,
      "context": "الحمد لله رب العالمين"
    }
  ]
}
```

### Analysis Endpoints

#### Get Word Analysis

Retrieve comprehensive analysis for a specific word.

**Request**
```
GET /api/analysis/word/:word
```

**Parameters**
- `word` (string, required): Word to analyze (Arabic)

**Response**
```json
{
  "word": "الحمد",
  "root": "حمد",
  "frequency": 157,
  "occurrences": [
    {"surah": 1, "verse": 1},
    {"surah": 2, "verse": 172}
  ],
  "meanings": ["praise", "gratitude", "commendation"],
  "relatedWords": ["حامد", "محمود", "حمادة"],
  "semanticField": ["شكر", "ثناء", "تعظيم"],
  "morphology": {
    "pattern": "فعل",
    "form": "noun",
    "gender": "masculine",
    "number": "singular"
  }
}
```

#### Calculate Similarity

Compare two words and calculate their similarity score.

**Request**
```
POST /api/analysis/similarity
Content-Type: application/json

{
  "word1": "الحمد",
  "word2": "الشكر"
}
```

**Response**
```json
{
  "word1": "الحمد",
  "word2": "الشكر",
  "similarity": 0.87,
  "metrics": {
    "levenshtein": 0.75,
    "cosine": 0.92,
    "contextual": 0.85
  },
  "commonContexts": [
    {"surah": 2, "verse": 172},
    {"surah": 31, "verse": 12}
  ]
}
```

#### Get Entropy Analysis

Retrieve entropy metrics for a surah or verse.

**Request**
```
GET /api/analysis/entropy/:surah/:verse?level=word
```

**Parameters**
- `surah` (integer, required): Surah number
- `verse` (integer, optional): Verse number (if omitted, returns surah-level entropy)
- `level` (string, optional): Entropy level - `word`, `root`, or `letter` (default: `word`)

**Response**
```json
{
  "surah": 1,
  "verse": 1,
  "level": "word",
  "entropy": 2.34,
  "maxEntropy": 3.5,
  "redundancy": 0.33,
  "uniqueElements": 7,
  "totalElements": 7
}
```

#### Get Markov Analysis

Retrieve Markov chain analysis for a surah.

**Request**
```
GET /api/analysis/markov/:surah?order=2
```

**Parameters**
- `surah` (integer, required): Surah number
- `order` (integer, optional): Markov order (1-5, default: 1)

**Response**
```json
{
  "surah": 1,
  "order": 2,
  "transitions": {
    "الحمد لله": {
      "رب": 1.0
    },
    "لله رب": {
      "العالمين": 1.0
    }
  },
  "stationaryDistribution": {...},
  "absorbingStates": [],
  "entropyRate": 1.23
}
```

#### Get Semantic Network

Retrieve semantic relationships between words or themes.

**Request**
```
GET /api/analysis/semantic-network?type=theme&theme=Tawhid
```

**Parameters**
- `type` (string, required): Network type - `word`, `theme`, or `root`
- `theme` (string, optional): Theme name (for theme networks)
- `limit` (integer, optional): Maximum nodes (default: 50)

**Response**
```json
{
  "nodes": [
    {"id": "توحيد", "label": "Tawhid", "frequency": 156},
    {"id": "الله", "label": "Allah", "frequency": 2698}
  ],
  "edges": [
    {"source": "توحيد", "target": "الله", "weight": 0.95}
  ],
  "clusters": [...]
}
```

### Visualization Endpoints

#### Generate Visualization

Create a visualization of analysis results.

**Request**
```
POST /api/visualization/generate
Content-Type: application/json

{
  "type": "heatmap",
  "data": "entropy",
  "format": "png",
  "width": 1200,
  "height": 800
}
```

**Parameters**
- `type` (string, required): Visualization type - `heatmap`, `network`, `timeline`, `distribution`
- `data` (string, required): Data to visualize
- `format` (string, optional): Output format - `png`, `svg`, `json` (default: `png`)
- `width` (integer, optional): Image width in pixels (default: 1200)
- `height` (integer, optional): Image height in pixels (default: 800)

**Response**
```
Binary image data (PNG/SVG) or JSON data
```

### Dashboard Endpoints

#### Get Dashboard Data

Retrieve aggregated data for the dashboard.

**Request**
```
GET /api/dashboard/summary
```

**Response**
```json
{
  "totalSurahs": 114,
  "averageEntropy": 2.85,
  "markovOrders": 5,
  "semanticFields": 10,
  "analysisStatus": "completed",
  "lastUpdated": "2025-12-27T10:30:00Z",
  "metrics": {
    "entropy": {...},
    "markov": {...},
    "glocality": {...}
  }
}
```

#### Export Analysis Results

Export analysis results in various formats.

**Request**
```
GET /api/export/results?format=json&scope=all
```

**Parameters**
- `format` (string, required): Export format - `json`, `csv`, `pdf`, `xlsx`
- `scope` (string, optional): Export scope - `all`, `surah`, `theme` (default: `all`)
- `surah` (integer, optional): Surah number (if scope is `surah`)
- `theme` (string, optional): Theme name (if scope is `theme`)

**Response**
```
File download or JSON data
```

## Error Handling

The API returns standard HTTP status codes and error messages:

### Error Response Format

```json
{
  "error": {
    "code": "INVALID_PARAMETER",
    "message": "The specified surah number is out of range",
    "details": {
      "parameter": "surah",
      "value": 115,
      "valid_range": "1-114"
    }
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_PARAMETER` | 400 | Invalid request parameter |
| `NOT_FOUND` | 404 | Requested resource not found |
| `UNAUTHORIZED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Access denied |
| `INTERNAL_ERROR` | 500 | Server error |
| `SERVICE_UNAVAILABLE` | 503 | Service temporarily unavailable |

## Rate Limiting

API requests are rate-limited to prevent abuse:

- **Authenticated Users**: 1000 requests per hour
- **Unauthenticated**: 100 requests per hour

Rate limit information is included in response headers:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1735300200
```

## Usage Examples

### Python Example

```python
import requests
import json

# Base URL
BASE_URL = "http://localhost:5173/api"

# Get word analysis
response = requests.get(
    f"{BASE_URL}/analysis/word/الحمد",
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)

word_data = response.json()
print(f"Word: {word_data['word']}")
print(f"Frequency: {word_data['frequency']}")
print(f"Root: {word_data['root']}")

# Calculate similarity
similarity_data = {
    "word1": "الحمد",
    "word2": "الشكر"
}

response = requests.post(
    f"{BASE_URL}/analysis/similarity",
    json=similarity_data,
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)

result = response.json()
print(f"Similarity: {result['similarity']}")
```

### JavaScript/TypeScript Example

```typescript
import axios from 'axios';

const BASE_URL = 'http://localhost:5173/api';
const token = 'YOUR_ACCESS_TOKEN';

// Get entropy analysis
async function getEntropyAnalysis(surah: number) {
  try {
    const response = await axios.get(
      `${BASE_URL}/analysis/entropy/${surah}`,
      {
        headers: { Authorization: `Bearer ${token}` }
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error fetching entropy data:', error);
  }
}

// Get semantic network
async function getSemanticNetwork(theme: string) {
  try {
    const response = await axios.get(
      `${BASE_URL}/analysis/semantic-network`,
      {
        params: { type: 'theme', theme },
        headers: { Authorization: `Bearer ${token}` }
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error fetching semantic network:', error);
  }
}
```

## Pagination

For endpoints that return lists, pagination is supported using `limit` and `offset` parameters:

```
GET /api/quran/search?q=الله&limit=20&offset=40
```

This returns results 40-59 (20 results per page, starting from offset 40).

## Versioning

The API is currently at version 1.0. Future versions will be indicated in the URL:

```
/api/v1/...
/api/v2/...
```

## Webhooks

Webhooks allow you to receive notifications when analysis is complete or data is updated. Contact support to set up webhooks for your application.

## Support

For API support and questions:

- **Documentation**: https://claudsh.dev/docs
- **GitHub Issues**: https://github.com/badreddine023/CLAUDSH/issues
- **Email**: api-support@claudsh.dev

---

**Last Updated**: December 2025  
**API Version**: 1.0.0
