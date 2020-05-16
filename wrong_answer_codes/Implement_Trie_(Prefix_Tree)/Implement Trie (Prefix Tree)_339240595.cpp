/*
 * Trie is similar to linkedlist with multiple next pointers (26 in this example). 
 * we have one pointer for each letter in the word.
 * eg: app:
 *          Trie()                  -----root trie-------
 *           /(next['a'])
 *         Trie()
 *          /(next['p'])
 *         Trie()
 *         /(next['p'])
 *        Trie()                    ------leaf trie------
 
 * we use a boolean variable to indicate a leaf node. 
*/
class Trie {
    Trie *next[26];
    bool isEnd;
public:
    /** Initialize your data structure here. */
    Trie() {
      for(int i = 0;i < 26; i++)
          next[i] = NULL;
        isEnd = false;
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Trie *temp = this;
        for(auto letter: word)
        {
            temp->next[letter - 'a'] = new Trie();
            temp = temp->next[letter-'a'];
        }
        temp->isEnd = true;
        
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Trie *temp = this;
        for(auto letter: word)
        {
            if(temp->next[letter - 'a'] == NULL)
                return false;
            temp = temp->next[letter - 'a'];
        }
        return temp->isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Trie *temp = this;
        for(auto letter: prefix)
        {
            if(temp->next[letter - 'a'] == NULL)
                return false;
            temp = temp->next[letter - 'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
