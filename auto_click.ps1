Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# =============================
# 狀態變數
# =============================
$script:click = $false
$script:workType = ""
$script:a = ""
$script:b = ""

# =============================
# 主視窗
# =============================
$form = New-Object System.Windows.Forms.Form
$form.Text = "報工系統"
$form.ClientSize = New-Object System.Drawing.Size(400, 350)
$form.StartPosition = "CenterScreen"
$form.FormBorderStyle = "FixedSingle"
$form.MaximizeBox = $false

$form.Font = New-Object System.Drawing.Font("Microsoft JhengHei UI", 12)

# =============================
# 左側輸入框
# =============================
$inputBox = New-Object System.Windows.Forms.TextBox
$inputBox.Multiline = $true
$inputBox.ScrollBars = "Vertical"
$inputBox.Location = New-Object System.Drawing.Point(15, 15)
$inputBox.Size = New-Object System.Drawing.Size(160, 310)

$form.Controls.Add($inputBox)


# =============================
# 報工類型 GroupBox
# =============================
$typeGroup = New-Object System.Windows.Forms.GroupBox
$typeGroup.Text = "報工站別"
$typeGroup.Location = New-Object System.Drawing.Point(195, 15)
$typeGroup.Size = New-Object System.Drawing.Size(190, 60)

$form.Controls.Add($typeGroup)


# 退平磨
$radioGrinding = New-Object System.Windows.Forms.RadioButton
$radioGrinding.Text = "退平磨"
$radioGrinding.Location = New-Object System.Drawing.Point(10, 25)
$radioGrinding.AutoSize = $true
$radioGrinding.Checked = $true

$typeGroup.Controls.Add($radioGrinding)


# 終檢刻字
$radioEngraving = New-Object System.Windows.Forms.RadioButton
$radioEngraving.Text = "終檢刻字"
$radioEngraving.Location = New-Object System.Drawing.Point(90, 25)
$radioEngraving.AutoSize = $true

$typeGroup.Controls.Add($radioEngraving)


# =============================
# 帳號按鈕
# =============================
$aButton = New-Object System.Windows.Forms.Button
$aButton.Text = "修改 A"
$aButton.Location = New-Object System.Drawing.Point(195, 90)
$aButton.Size = New-Object System.Drawing.Size(190, 32)
$form.Controls.Add($aButton)


$bButton = New-Object System.Windows.Forms.Button
$bButton.Text = "修改 B"
$bButton.Location = New-Object System.Drawing.Point(195, 130)
$bButton.Size = New-Object System.Drawing.Size(190, 32)
$form.Controls.Add($bButton)


$cButton = New-Object System.Windows.Forms.Button
$cButton.Text = "修改 C"
$cButton.Location = New-Object System.Drawing.Point(195, 170)
$cButton.Size = New-Object System.Drawing.Size(190, 32)
$form.Controls.Add($cButton)


# =============================
# 狀態
# =============================
$label = New-Object System.Windows.Forms.Label
$label.Text = "未選擇工號"
$label.Location = New-Object System.Drawing.Point(195, 215)
$label.Size = New-Object System.Drawing.Size(190, 40)

$form.Controls.Add($label)


# =============================
# 開始報工 - 最下面
# =============================
$startButton = New-Object System.Windows.Forms.Button
$startButton.Text = "開始報工"
$startButton.Location = New-Object System.Drawing.Point(195, 290)
$startButton.Size = New-Object System.Drawing.Size(190, 35)

$form.Controls.Add($startButton)


# =============================
# 修改帳號
# =============================
function Set-Value {
    param(
        [string]$VariableName
    )

    switch ($VariableName) {

        "a" {
            $script:a = "123456"
            $script:b = "654321"
            $label.Text = "報工帳號已切換成：$script:a"
            $script:click = $true
        }

        "b" {
            $script:a = "111111"
            $script:b = "222222"
            $label.Text = "報工帳號已切換成：$script:a"
            $script:click = $true
        }

        "c" {
            $script:a = "333333"
            $script:b = "444444"
            $label.Text = "報工帳號已切換成：$script:a"
            $script:click = $true
        }
    }
}


# =============================
# 開始報工
# =============================
function Start-Work {

    if (-not $script:click) {
        $label.Text = "請先選擇工號"
        return
    }

    $text = $inputBox.Text

    if ([string]::IsNullOrWhiteSpace($text)) {
        $label.Text = "請輸入報工資料"
        return
    }

    $label.Text = "開始報工"

    # 之後 Windows UI Automation 放這裡
}


# =============================
# Events
# =============================
$aButton.Add_Click({
    Set-Value "a"
})

$bButton.Add_Click({
    Set-Value "b"
})

$cButton.Add_Click({
    Set-Value "c"
})

$startButton.Add_Click({
    Start-Work
})


$radioGrinding.Add_CheckedChanged({

    if ($radioGrinding.Checked) {
        $script:workType = "退平磨"
    }

})

$radioEngraving.Add_CheckedChanged({

    if ($radioEngraving.Checked) {
        $script:workType = "終檢刻字"
    }

})

# =============================
# 顯示
# =============================
[void]$form.ShowDialog()
