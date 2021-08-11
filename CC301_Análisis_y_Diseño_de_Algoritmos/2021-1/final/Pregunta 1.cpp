#include <bits/stdc++.h>
using namespace std;
#define N 3
struct Node
{
    Node *parent;
    int costoCamino;
    int costo;
    int hijo;
    int padre;
    bool assigned[N];
};
Node *newNode(int x, int y, bool assigned[],
              Node *parent)
{
    Node *node = new Node;

    for (int j = 0; j < N; j++)
        node->assigned[j] = assigned[j];
    node->assigned[y] = true;

    node->parent = parent;
    node->hijo = x;
    node->padre = y;

    return node;
}
int calculateCost(int costMatrix[N][N], int x,
                  int y, bool assigned[])
{
    int costo = 0;
    bool available[N] = {true};
    for (int i = x + 1; i < N; i++)
    {
        int min = INT_MAX, minIndex = -1;
        for (int j = 0; j < N; j++)
        {
            if (!assigned[j] && available[j] &&
                costMatrix[i][j] < min)
            {
                minIndex = j;
                min = costMatrix[i][j];
            }
        }
        costo += min;
        available[minIndex] = false;
    }
    return costo;
}
struct comp
{
    bool operator()(const Node *lhs,
                    const Node *rhs) const
    {
        return lhs->costo > rhs->costo;
    }
};
void printAssignments(Node *min)
{
    if (min->parent == NULL)
        return;

    printAssignments(min->parent);
    cout << "Ciudad " << char(min->hijo + 'A')
         << " contenedor " << min->padre << endl;
}


int findMinCost(int costMatrix[N][N])
{

    priority_queue<Node *, std::vector<Node *>, comp> pq;
    bool assigned[N] = {false};
    Node *root = newNode(-1, -1, assigned, NULL);
    root->costoCamino = root->costo = 0;
    root->hijo = -1;
    pq.push(root);
    while (!pq.empty())
    {
        Node *min = pq.top();
        pq.pop();
        int i = min->hijo + 1;
        if (i == N)
        {
            printAssignments(min);
            return min->costo;
        }
        for (int j = 0; j < N; j++)
        {

            if (!min->assigned[j])
            {
                Node *child = newNode(i, j, min->assigned, min);
                child->costoCamino = min->costoCamino + costMatrix[i][j];
                child->costo = child->costoCamino +
                              calculateCost(costMatrix, i, j, child->assigned);
                pq.push(child);
            }
        }
    }
}

int main()
{
    int costMatrix[N][N] =
        {
            {30, 40, 70},
            {60, 20, 10},
            {40, 90, 30}};

    cout << "El costo es : "
         << findMinCost(costMatrix)<<endl;
    return 0;
}

