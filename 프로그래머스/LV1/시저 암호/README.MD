# Lv1 시저 암호
 [시저 암호 링크]("https://school.programmers.co.kr/learn/courses/30/lessons/12926")

### 테스트결과
 Time:3.49ms, Memory:9.24MB


### 문제설명
<p>어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.  예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.</p>

<h5>제한 조건</h5>

<ul>
    <li>공백은 아무리 밀어도 공백입니다.</li>
    <li>s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.</li>
    <li>s의 길이는 8000이하입니다.</li>
    <li>n은 1 이상, 25이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
<thead><tr>
    <th>s</th>
    <th>n</th>
    <th>result</th>
</tr>
</thead>
<tbody><tr>
    <td>"AB"</td>
    <td>1</td>
    <td>"BC"</td>
</tr>
<tr>
    <td>"z"</td>
    <td>1</td>
    <td>"a"</td>
</tr>
<tr>
    <td>"a B z"</td>
    <td>4</td>
    <td>"e F d"</td>
</tr>
</tbody>
</table>