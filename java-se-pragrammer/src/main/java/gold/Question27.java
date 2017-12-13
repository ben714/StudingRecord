package gold;

import gold.bean.Candidate;

/**
 * 把今天最好的表现当作明天最新的起点．．～
 * いま 最高の表現 として 明日最新の始発．．～
 * Today the best performance  as tomorrow newest starter!
 * Created by IntelliJ IDEA.
 * <p>
 * author: xiaomo
 * github: https://github.com/xiaomoinfo
 * email : xiaomo@xiaomo.info
 * QQ    : 83387856
 * Date  : 2017/12/13 19:41
 * desc  :
 * Copyright(©) 2017 by xiaomo.
 */
public class Question27 {
    public static void main(String[] args) {
        Candidate c = null;
        Candidate c1 = null;
        try {
            c = new Candidate("", 1);
            c1 = new Candidate("", 1);
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println(c);
        System.out.println(c1);
    }

}
