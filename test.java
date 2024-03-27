import java.util.List;
public class MyClass {
    public int sum(List<Integer> a) {
        int s = 0;
        for (int v: a) {
            s += v;
        }
        return s;
    }
}