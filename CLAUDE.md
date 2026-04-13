# Instruções permanentes

Sempre faça commit e push diretamente na branch main.
Nunca crie branches separadas.
Nunca abra Pull Requests.
Trabalhe sempre na main diretamente.

## Regras obrigatórias de git para geração de posts

- Antes de qualquer commit, execute `git checkout main` para garantir que está na branch correta.
- Se o repositório estiver em outra branch, retorne para a main com `git checkout main` antes de escrever qualquer arquivo.
- Nunca commite posts, prompts de carrossel ou atualizações do progresso.md em branches intermediárias.
- O fluxo correto é: escrever arquivo → `git add` → `git commit` → `git push origin main`.
- Se o ambiente de sessão criar uma branch automática (ex: claude/alguma-branch), ignore-a e trabalhe na main mesmo assim.
- Nunca faça merge de branches — os arquivos já devem nascer na main.
