using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[][] newPuzzle = makePuzzle2();
            sudokuSolver(newPuzzle);
            PrintPuzzle(newPuzzle);
            Console.In.ReadLine();
        }

        static void PrintPuzzle(int[][] puzzle)
        {
            for (int i = 0; i < puzzle.Length; i++)
            {
                for (int j = 0; j < puzzle[0].Length; j++)
                {
                    Console.Out.Write(puzzle[i][j]);
                    Console.Out.Write(" , ");
                    
                }
                Console.Out.WriteLine();
            }
            
        }

        static int[][] makePuzzle()
        {
            int[][] puzzle = new int[9][];
            puzzle[0] = new int[9] { 0, 0, 5, 4, 7, 0, 0, 0, 2 };
            puzzle[1] = new int[9] { 0, 0, 2, 0, 0, 0, 7, 0, 0 };
            puzzle[2] = new int[9] { 0, 7, 0, 0, 0, 9, 8, 0, 1 };
            puzzle[3] = new int[9] { 2, 0, 0, 0, 3, 7, 5, 0, 4 };
            puzzle[4] = new int[9] { 0, 4, 0, 6, 0, 1, 0, 9, 0 };
            puzzle[5] = new int[9] { 3, 0, 1, 8, 4, 0, 0, 0, 7 };
            puzzle[6] = new int[9] { 8, 0, 4, 5, 0, 0, 0, 7, 0 };
            puzzle[7] = new int[9] { 0, 0, 6, 0, 0, 0, 2, 0, 0 };
            puzzle[8] = new int[9] { 7, 0, 0, 0, 8, 3, 4, 0, 0 };
            return puzzle;
        }

        static int[][] makePuzzle2()
        {
            int[][] puzzle = new int[9][];
            puzzle[0] = new int[9] { 0, 2, 7, 0, 0, 0, 0, 0, 1 };
            puzzle[1] = new int[9] { 0, 0, 0, 0, 9, 5, 0, 3, 4 };
            puzzle[2] = new int[9] { 0, 9, 0, 0, 0, 1, 0, 0, 0 };
            puzzle[3] = new int[9] { 1, 0, 0, 0, 0, 6, 0, 5, 0 };
            puzzle[4] = new int[9] { 4, 0, 0, 0, 3, 0, 0, 0, 2 };
            puzzle[5] = new int[9] { 0, 8, 0, 1, 0, 0, 0, 0, 9 };
            puzzle[6] = new int[9] { 0, 0, 0, 5, 0, 0, 0, 1, 0 };
            puzzle[7] = new int[9] { 8, 3, 0, 6, 1, 0, 0, 0, 0 };
            puzzle[8] = new int[9] { 7, 0, 0, 0, 0, 0, 3, 4, 0 };
            return puzzle;
        }

        static int[][] sudokuSolver(int[][] puzzle)
        {
            List<int> nextEmpty = getNextEmpty(puzzle, 0, 0);
            if (solve(puzzle, nextEmpty[0], nextEmpty[1])) {
                return puzzle;
            }
            else
            {
                throw new Exception("Not solvable");
            }
        }

        static bool solve(int[][] puzzle, int i, int j)
        {
            bool result = false;

            if (filled(puzzle)) {
                return true;
            }

            List<int> possibilities = getPossibilities(puzzle, i, j);

            

            foreach (int x in possibilities)
            {
                puzzle[i][j] = x;
                List<int> nextEmpty = getNextEmpty(puzzle, i, j);
                if (nextEmpty == null)
                {
                    return true;
                }
                result = solve(puzzle, nextEmpty[0], nextEmpty[1]);
                if (!result) {
                    puzzle[i][j] = 0;
                }
                else
                {
                    return true;
                }
            }

            return false;
        }

        static bool filled(int[][] puzzle)
        {
            for (int i = 0; i < puzzle.Length; i++)
            {
                for (int j = 0; j < puzzle[i].Length; j++)
                {
                    if (puzzle[i][j] == 0) {
                        return false;
                    }
                        
                }
            }

            return true;
        }

        static List<int> getPossibilities(int[][] puzzle, int i, int j)
        {
            List<int> rowPossibilities = getRowPossibilities(puzzle, i);
            List<int> colPossibilities = getColPossibilities(puzzle, j);
            List<int> gridPossibilities = getGridPossibilities(puzzle, i, j);

            return gridPossibilities.Intersect(rowPossibilities).Intersect(colPossibilities).ToList();

        }

        static List<int> getRowPossibilities(int[][] puzzle, int row)
        {
            HashSet<int> result = new HashSet<int>();
            for (int i = 1; i < 10; i++)
            {
                result.Add(i);
            }

            for (int i = 0; i < puzzle[row].Length; i++)
            {
                if (puzzle[row][i] > 0)
                {
                    result.Remove(puzzle[row][i]);
                }
            }

            return result.ToList();
        }

        static List<int> getColPossibilities(int[][] puzzle, int col)
        {
            HashSet<int> result = new HashSet<int>();
            for (int i = 1; i < 10; i++)
            {
                result.Add(i);
            }

            for (int i = 0; i < puzzle.Length; i++)
            {
                if (puzzle[i][col] > 0)
                {
                    result.Remove(puzzle[i][col]);
                }
            }

            return result.ToList();
        }

        static List<int> getGridPossibilities(int[][] puzzle, int row, int col)
        {
            HashSet<int> result = new HashSet<int>();
            for (int i = 1; i < 10; i++)
            {
                result.Add(i);
            }

            int gridRow = row / 3;
            int gridCol = col / 3;

            for (int i = gridRow * 3; i < gridRow * 3 + 3; i++)
            {
                for (int j = gridCol * 3; j < gridCol * 3 + 3; j++)
                {
                    if (puzzle[i][j] > 0)
                    {
                        result.Remove(puzzle[i][j]);
                    }
                }
            }

            return result.ToList();
        }


        static List<int> getNextEmpty(int[][] puzzle, int i, int j)
        {
            List<int> result = new List<int>();

            for (int row = i; row < puzzle.Length; row ++)
            {
                for (int col = 0; col < puzzle[0].Length; col++)
                {
                    if (puzzle[row][col] == 0) {
                        result.Add(row);
                        result.Add(col);
                        return result;
                    }
                }
            }

            return null;
        }

    }
}
