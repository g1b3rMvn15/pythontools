# Importa o módulo do Active Directory
Import-Module ActiveDirectory

# Obtém todos os usuários habilitados (ativos)
$usuariosAtivos = Get-ADUser -Filter {Enabled -eq $true} -Properties Name, SamAccountName, EmailAddress, Enabled, whenCreated, LastLogonDate

# Seleciona e formata as propriedades desejadas
$usuariosFormatados = $usuariosAtivos | Select-Object `
    Name,
    SamAccountName,
    EmailAddress,
    @{Name="Status"; Expression={if ($_.Enabled) {'Ativo'} else {'Inativo'}}},
    @{Name="DataCriacao"; Expression={$_.whenCreated}},
    @{Name="UltimoLogon"; Expression={$_.LastLogonDate}}

# Exporta para CSV (opcional)
$usuariosFormatados | Export-Csv -Path "Usuarios_Ativos_AD.csv" -NoTypeInformation -Encoding UTF8

# Exibe no console
$usuariosFormatados
