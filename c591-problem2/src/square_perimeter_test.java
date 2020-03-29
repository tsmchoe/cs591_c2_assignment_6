import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class square_perimeter_test {

    @Test
    public void test() throws Exception{
        assertEquals(null, problem_2.squarePerimeter(-2.0));
        assertEquals(null, problem_2.squarePerimeter(-4.0));
        assertEquals(null, problem_2.squarePerimeter( -6.0));
        assertEquals(8, problem_2.squarePerimeter(2.0) , 1);
        assertEquals(16, problem_2.squarePerimeter(4.0) , 1);
        assertEquals(36, problem_2.squarePerimeter(9.0), 1);
    }
}
