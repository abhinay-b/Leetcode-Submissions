class RandomizedSet {
private:
    unordered_set<int>randSet;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        srand(time(NULL));
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the 
        specified element. */
    bool insert(int val) {
        bool flag  = randSet.find(val) == randSet.end();
        randSet.insert(val);
        return flag;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. 
        */
    bool remove(int val) {
        bool flag = randSet.find(val) != randSet.end();
        if(flag)
            randSet.erase(val);
        return flag;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int idx = rand() % randSet.size();
        return *(std::next(randSet.begin(),idx));
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
