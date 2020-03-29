import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class square_area_test {

    @Test
    public void test() throws Exception{
        assertEquals(null, problem_2.squareArea(-2.0));
        assertEquals(null, problem_2.squareArea(-4.0));
        assertEquals(null, problem_2.squareArea( -6.0));
        assertEquals(4, problem_2.squareArea(2.0) , 1);
        assertEquals(16, problem_2.squareArea(4.0) , 1);
        assertEquals(81, problem_2.squareArea(9.0), 1);
    }
}
