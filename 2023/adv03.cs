using System.Text;
using System.Text.RegularExpressions;

const int BufferSize = 128;
List<string> lines = new();
int sumP1 = 0, sumP2 = 0;
Regex regexNumber = new(@"\d+");
Regex regexStar = new(@"\*");

using (var fileStream = File.OpenRead("adv03.txt"))
{
    using var streamReader = new StreamReader(fileStream, Encoding.UTF8, true, BufferSize);

    string? line;
    while ((line = streamReader.ReadLine()) != null)
    {
        lines.Add(line);
    }
}

for (int i = 0; i < lines.Count; ++i)
{
    foreach (Match match in regexNumber.Matches(lines[i]))
    {
        int minX = Math.Max(match.Index - 1, 0);
        int maxX = Math.Min(match.Index + match.Length + 1, lines[i].Length);

        if (
            i > 0 && lines[i - 1].Substring(minX, maxX - minX).Replace(".", "").Length > 0 
            || lines[i].Substring(minX, maxX - minX).Replace(".", "").Length > match.Length
            || i < (lines.Count - 1) && lines[i + 1].Substring(minX, maxX - minX).Replace(".", "").Length > 0
        )
            sumP1 += int.Parse(match.Value);
    }

    foreach (Match match in regexStar.Matches(lines[i]))
    {
        int minX = Math.Max(match.Index - 1, 0);
        int maxX = Math.Min(match.Index + 1, lines[i].Length);

        int numberOfNumbers = 0;
        int power = 1;

        for (int j = Math.Max(i - 1, 0); j <= Math.Min(i + 1, lines.Count); ++j)
        {
            int minXLine = minX;
            int maxXLine = maxX;

            while (minXLine != 0 && int.TryParse(lines[j][minXLine].ToString(), out int _))
                --minXLine;

            while (maxXLine < lines[j].Length && int.TryParse(lines[j][maxXLine].ToString(), out int _))
                ++maxXLine;

            foreach (Match matchNumber in regexNumber.Matches(lines[j][minXLine..maxXLine]))
            {
                ++numberOfNumbers;
                power *= int.Parse(matchNumber.Value);
            }
        }

        if (numberOfNumbers >= 2)
            sumP2 += power;
    }
}


Console.WriteLine($"Part 1: {sumP1}");
Console.WriteLine($"Part 2: {sumP2}");
