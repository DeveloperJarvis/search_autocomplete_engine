# 📌 Low Level Design: Search Autocomplete Engine

## 🎯 Problem Statement

Design a search autocomplete engine that:

- Suggests queries as the user types
- Uses **Trie** for fast prefix search
- Ranks suggestions based on **frequency of usage**
- Supports dynamic updates (new searches improve ranking)

---

## 🧠 Core Concepts Used

- **Trie (Prefix Tree)** → Fast prefix-based lookup
- **Frequency Ranking** → Popular searches appear first
- **Data Indexing** → Efficient retrieval and updates
- **String Algorithms** → Prefix matching

---

## 🏗 High-Level Architecture

```
User Input
   ↓
AutocompleteService
   ↓
TrieIndex ─── FrequencyStore
   ↓
Ranker
   ↓
Top-K Suggestions
```

---

## 📦 Core Components & Responsibilities

---

### 1⃣ `AutocompleteService`

**Role:** Entry point for the system

**Responsibilities:**

- Accept user input (prefix)
- Fetch autocomplete suggestions
- Update frequency when a query is finalized

**Key Operations:**

- `getSuggestions(prefix, limit)`
- `recordQuery(query)`

---

### 2⃣ `TrieNode`

**Role:** Fundamental unit of the Trie

**Attributes:**

- `children` → mapping of characters to TrieNode
- `isEndOfWord` → indicates complete query
- `frequency` → number of times this query was searched
- `topSuggestions` → cached top-K suggestions under this prefix

**Why store top suggestions?**

- Avoid recomputing rankings on every keystroke
- Improves response time from **O(N)** to **O(1)** per node

---

### 3⃣ `TrieIndex`

**Role:** Stores and manages all search queries

**Responsibilities:**

- Insert new queries
- Search by prefix
- Maintain prefix-based hierarchy

**Key Operations:**

- `insert(query)`
- `searchPrefix(prefix)`
- `updateFrequency(query)`

---

### 4⃣ `FrequencyStore`

**Role:** Tracks popularity of queries

**Responsibilities:**

- Maintain global frequency count
- Provide ranking signals to Trie

**Storage Options:**

- In-memory dictionary (small scale)
- Redis / Key-Value store (large scale)

---

### 5⃣ `Ranker`

**Role:** Orders suggestions by relevance

**Ranking Criteria (can be extended):**

1. Search frequency
2. Lexicographical order (tie-breaker)
3. Recency (optional)

**Key Operation:**

- `rank(candidates, limit)`

---

## 🔁 Data Flow (Autocomplete Request)

1. User types: `"ap"`
2. `AutocompleteService` receives prefix
3. `TrieIndex` navigates to `"ap"` node
4. Fetches stored `topSuggestions`
5. `Ranker` sorts if needed
6. Returns top-K suggestions

⏱ **Time Complexity:**

- Trie traversal: **O(length of prefix)**
- Suggestion retrieval: **O(K)**

---

## 🔄 Data Flow (Query Finalized)

1. User searches `"apple iphone"`
2. `AutocompleteService.recordQuery()`
3. Trie inserts or updates query
4. Frequency incremented
5. Top-K lists updated bottom-up

---

## 🧪 Edge Cases Considered

- Empty prefix → return trending searches
- New unseen query → added with frequency = 1
- Prefix not found → return empty list
- Case normalization (e.g., lowercase everything)

---

## ⚙ Design Decisions Explained

### Why Trie?

- Faster than scanning all strings
- Prefix search in **O(L)** instead of **O(N)**

### Why store top-K at each node?

- Avoid DFS for every keystroke
- Makes autocomplete feel instantaneous

### Why separate Ranker?

- Clean separation of concerns
- Easy to change ranking logic later

---

## 📈 Scalability Considerations

| Problem           | Solution                    |
| ----------------- | --------------------------- |
| High memory usage | Compress Trie / limit top-K |
| Large dataset     | Sharded Trie                |
| High read traffic | Read replicas               |
| Cold start        | Preload popular queries     |
| Multi-language    | Unicode-aware Trie          |

---

## 🔐 Optional Enhancements

- Personalization (user-specific history)
- Time-decay ranking
- Spelling correction
- Fuzzy matching
- Analytics dashboard

---

## 📊 Complexity Summary

| Operation        | Complexity          |
| ---------------- | ------------------- |
| Insert query     | O(L)                |
| Search prefix    | O(L + K)            |
| Update frequency | O(L)                |
| Memory           | O(total characters) |

---

## 🧠 Interview Tip

If asked:

> _“Why not use a HashMap?”_

Answer:

> HashMaps don’t support prefix search efficiently. Trie guarantees fast prefix lookup regardless of dataset size.

---

## ✅ Final Takeaway

This design:

- Is **clean**
- Is **highly performant**
- Scales well
- Matches **real-world autocomplete systems** (Google, Amazon, etc.)
