# Lv1 문자열 내 p와 y의 개수
 [문자열 내 p와 y의 개수 링크]("https://school.programmers.co.kr/learn/courses/30/lessons/12916")

### 테스트결과
 Time:0.00ms, Memory:9.23MB

### 문제설명
<p>대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.</p>

<p>예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.</p>

<h5>제한사항</h5>

<ul>
    <li>문자열 s의 길이 : 50 이하의 자연수</li>
    <li>문자열 s는 알파벳으로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
<thead><tr>
    <th>s</th>
    <th>answer</th>
</tr>
</thead>
<tbody><tr>
    <td>"pPoooyY"</td>
    <td>true</td>
</tr>
<tr>
    <td>"Pyy"</td>
    <td>false</td>
</tr>
</tbody>
</table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.</p>

<p>입출력 예 #2<br>
'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.</p>

<p>※ 공지 - 2021년 8월 23일 테스트케이스가 추가되었습니다.</p>
