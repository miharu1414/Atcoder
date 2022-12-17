// ABC281 - Eで使用

/*


struct multiset_sum{
    ll low_sum, high_sum, partition;
    multiset<ll> low_st, high_st;
 
    multiset_sum(){low_sum = high_sum = partition = 0;}
    int size(){return (int)low_st.size() + (int)high_st.size();}
    void insert(ll x){
        if(high_st.size() && *high_st.begin() <= x)high_st.insert(x),high_sum += x;
        else low_st.insert(x),low_sum += x;
        adjust();
    }
    void erase(ll x){
        if(high_st.size() && *high_st.begin() <= x)high_st.erase(high_st.find(x)),high_sum -= x;
        else low_st.erase(low_st.find(x)),low_sum -= x;
        adjust();
    }
    void adjust(){
        while((int)low_st.size() > partition){
            int low_mx = *low_st.rbegin();
            high_sum += low_mx;
            low_sum -= low_mx;
            high_st.insert(low_mx);
            low_st.erase(low_st.find(low_mx));
        }
        while((int)low_st.size() < partition && high_st.size()){
            int high_mn = *high_st.begin();
            low_sum += high_mn;
            high_sum -= high_mn;
            low_st.insert(high_mn);
            high_st.erase(high_st.find(high_mn));
        }
    }
    void adjust(ll x){
        partition = x;
        adjust();
    }
    ll get_lowsum(int k){
        //小さい方からk個の和
        if(k<0)return 0;
        if(k>=size())return low_sum+high_sum;
        adjust(k);
        return low_sum;
    }
    ll get_highsum(int k){
        //大きい方からk個の和
        if(k<0)return 0;
        if(k>=size())return low_sum+high_sum;
        int lk = size()-k;
        adjust(lk);
        return high_sum;
    }
};

// multiset_sumを宣言　　　mulitiset_sum st;
// 挿入 st.insert(x);
// 削除 st.erase(x);
// 小さい方からk個の和 st.get_lowsum(k);
// 大きい方からk個の和 st.get_highsum(k);

*/