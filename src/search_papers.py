import arxiv
from utils import format_date

def search_papers(query, max_results=10, sort_by="relevance"):
    """
    arXivライブラリを使用して論文を検索し、結果をリストとして返す。
    
    :param query: 検索クエリ
    :param max_results: 取得する最大結果数（デフォルトは10）
    :param sort_by: ソート基準（'relevance', 'submittedDate', 'lastUpdatedDate'）
    :return: 論文情報のリスト（辞書形式）
    """
    # ソート基準の選択に応じたソートオプションを設定
    sort_criteria = {
        "relevance": arxiv.SortCriterion.Relevance,
        "submittedDate": arxiv.SortCriterion.SubmittedDate,
        "lastUpdatedDate": arxiv.SortCriterion.LastUpdatedDate
    }
    sort_criterion = sort_criteria.get(sort_by, arxiv.SortCriterion.Relevance)

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=sort_criterion
    )

    results = []
    for result in search.results():
        paper = {
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "summary": result.summary.strip(),
            "published": format_date(result.published),
            "arxiv_id": result.entry_id.split('/')[-1]
        }
        results.append(paper)

    return results
