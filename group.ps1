param (
    [Parameter(Mandatory = $true)]
    [string]$GroupName,

    [string]$CsvPath = "group_parent_direct.csv"
)

Import-Module ActiveDirectory

# Função recursiva para pegar grupos-pai pelo atributo memberOf do grupo filho
function Get-ParentGroupsByMemberOf {
    param (
        [string]$GroupDN,
        [int]$Level = 0
    )

    if ($visitedGroups.ContainsKey($GroupDN)) {
        return
    }
    $visitedGroups[$GroupDN] = $true

    $group = Get-ADGroup -Identity $GroupDN
    $result += [PSCustomObject]@{
        Level = $Level
        GroupName = $group.Name
        DistinguishedName = $GroupDN
    }

    # Pega grupos pai do atributo memberOf
    $parentsDN = $group.memberof
    if ($parentsDN) {
        foreach ($parentDN in $parentsDN) {
            Get-ParentGroupsByMemberOf -GroupDN $parentDN -Level ($Level + 1)
        }
    }
}

$group = Get-ADGroup -Filter "Name -eq '$GroupName'"
if (-not $group) {
    Write-Host "❌ Grupo '$GroupName' não encontrado." -ForegroundColor Red
    exit
}

Write-Host "✅ Grupo inicial encontrado: $($group.Name)"
Write-Host "DN do grupo inicial: $($group.DistinguishedName)"
Write-Host "`n🔁 Buscando grupos-pai recursivamente pelo atributo memberOf:`n"

$visitedGroups = @{}
$result = @()

Get-ParentGroupsByMemberOf -GroupDN $group.DistinguishedName -Level 0

# Exibe hierarquia com indentação
foreach ($item in $result | Sort-Object Level) {
    $indent = " " * ($item.Level * 4)
    Write-Host "$indent- $($item.GroupName) [$($item.DistinguishedName)]"
}

$result | Sort-Object Level | Export-Csv -Path $CsvPath -NoTypeInformation -Encoding UTF8

Write-Host "`n📁 Exportado arquivo CSV: $CsvPath" -ForegroundColor Cyan
